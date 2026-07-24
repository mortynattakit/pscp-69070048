"""this code will tell the minimum days that u need to workout"""
import math
pushup = int(input())
situp = int(input())
getup = int(input())
run = int(input())

pushuppd = int(input())
situppd = int(input())
getuppd = int(input())
runpd = int(input())

pushuptotal = math.floor(pushup // pushuppd)
situptotal = math.floor(situp // situppd)
getuptotal = math.floor(getup // getuppd)
runtotal = math.floor(run // runpd)

print(max(pushuptotal, situptotal, getuptotal, runtotal))
