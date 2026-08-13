"""this code will tell the minimum days that u need to workout"""
import math
pushup = int(input())
situp = int(input())
getup = int(input())
run = int(input())

pushuppd = int(input())
situppd = int(input())
runpd = int(input())
getuppd = int(input())

pushuptotal = math.ceil(pushup / pushuppd)
situptotal = math.ceil(situp / situppd)
getuptotal = math.ceil(getup / getuppd)
runtotal = math.ceil(run / runpd)

print(max(pushuptotal, situptotal, runtotal, getuptotal))
