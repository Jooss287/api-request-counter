import api_counter as apiCounter
import urllib.request as socket
import urllib.error as urlerr
from urllib.parse import quote

api_url = ""

counter = apiCounter.APIRequestCounter(5, apiCounter.TimeEnum.S)

for i in range(50):
    counter.requestCount(True)
    response = socket.urlopen(api_url)

# for i in range(50):
#     if counter.requestCount(False) is True:
#         response = socket.urlopen(api_url)
#     else:
#         print("False")

    # print(response)
    # res_code = response.getcode()
    # print(res_code)
    # response_body = response.read().decode('utf-8')
    # print(response_body)
        
#         return self._get_response_code(res_code, response_body)
#     except urlerr.HTTPError as err:
#         err_return = {"code": err.code,
#                         "explain": err.reason,
#                         "body": ""}
#         print("HTTP Error !!")
#         print(err.reason)
#         print("(", i+1, "/", 5, ")retry...")
#         time.sleep(0.5)
#     except urlerr.URLError as err:
#         err_return = {"explain": err.reason,
#                         "body": ""}
#         print("URL Error !!")
#         print(err.reason)
#         print("(", i+1, "/", 5, ")retry...")
#         time.sleep(0.5)
# err_log_dict = err_return.copy()
# err_log_dict["url"] = request_url
# self._api_error_list.append(err_log_dict)
# return err_return