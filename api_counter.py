import datetime
import time
import concurrent.futures
from enum import IntEnum, auto
from threading import Thread

class TimeEnum(IntEnum):
    S = 1
    M = S*60
    H = M*60
    D = H*24

# 일정 시간에 따른 접근 횟수 기록
class LimitCountPerTime:
    _api_request_time = []
    _count_value : int

    def __init__(self, count_value : int, per_time : TimeEnum):
        self._per_time = per_time
        self._setCountInput(count_value)

    def _setCountInput(self, count_value: int):
        assert count_value > 0, "count value must input higher than 0"
        self._count_value = count_value
    
    def changeCondition(self, count_value: int):
        self._setCountInput(count_value)

    def checkRequestCondition(self, now : datetime.datetime, sync: bool):
        if sync is True:
            self.checkSyncCondition(now)
        else:
            self.checkASyncCondition(now)

    def checkSyncCondition(self, now : datetime.datetime):
        self._api_request_time.append(now)

        api_cnt = len(self._api_request_time)
        if api_cnt < self._count_value:
            return

        span_time = (self._api_request_time[api_cnt - 1] - self._api_request_time[0])
        
        if span_time.total_seconds() < self._per_time:
            time.sleep(self._per_time*1.05 - span_time.total_seconds())   # 모자란 시간보다 5%더 대기시키고 진행
        del self._api_request_time[0]

    def checkAsyncCondition(self, now : datetime.datetime):
        self._api_request_time.append(now)

        api_cnt = len(self._api_request_time)
        if api_cnt < self._count_value:
            return True

        span_time = (now - self._api_request_time[0])
        
        if span_time.total_seconds() < self._per_time:
            return False
        else:
            self._api_request_time.append(now)
            del self._api_request_time[0]
        return True

class APIRequestCounter:
    _count_limit : []
    
    def __init__(self):
        self._start_condition = False
        
    def __init__(self, count_value : int, per_time : TimeEnum):
        self._count_limit = []
        self.addCondition(count_value, per_time)

    def addCondition(self, count_value: int, per_time: TimeEnum):
        is_existed = False
        if len(self._count_limit) is not 0:
            for condition in self._count_limit:
                if condition.checkTimeType() is per_time:
                    is_existed = True
                    condition.changeCondition(count_value)
        
        if is_existed is False:
            self._count_limit.append(LimitCountPerTime(count_value, per_time))
        
        self._start_condition = True

    def requestCount(self, sync = True):
        assert self._start_condition is True, "doen't have start condition"

        now = datetime.datetime.now()
        thread_list = []
        is_valid = True

        if sync is True:    # sync request count is wait for request time
            for counter in self._count_limit:
                th = Thread(target=counter.checkSyncCondition, args=(now,))
                thread_list.append(th)
                th.start()
            for th in thread_list:
                th.join()
        else:  # async request count is if it can request, return true
            for counter in self._count_limit:
                is_valid &= counter.checkAsyncCondition(now)
            #     thread_list.append(concurrent.futures.ThreadPoolExecutor().submit(counter.checkAsyncCondition, args=(now,)))
            # for th in thread_list:
            #     is_valid &= th.result()
        
        return is_valid
        

