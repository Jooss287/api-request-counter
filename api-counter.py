import datetime
import time
from enum import Enum, auto

class TimeEnum(Enum):
    S = auto()
    M = auto()
    H = auto()
    D = auto()

# 일정 시간에 따른 접근 횟수 기록
class LimitCountPerTime:
    condition : dict

    def __init__(self, time : TimeEnum, per_value : int):
        self._limit_time = time
        self._per_value = per_value
    
    # def checkCondition:
        # api_cnt = len(CommToApiServer.__api_start_time)
        #     span_time = (CommToApiServer.__api_start_time[api_cnt - 1]
        #                  - CommToApiServer.__api_start_time[0])

        #     if (span_time.total_seconds() < 1) & (api_cnt >= 100):
        #         time.sleep(1 - span_time.total_seconds() + 0.3)
        #     if api_cnt >= 100:
        #         del CommToApiServer.__api_start_time[0]

class APIRequestConter:
    _api_request_time = []
    _count_limit : LimitCountPerTime

    def __init__(self):
        pass

    def isValid(self):
        if len(self._api_request_time) is 0:
            self._api_request_time.append(datetime.datetime.now())
            return True
        else:
            # check condition

            
            self._api_request_time.append(datetime.datetime.now())
            return False
        
        
