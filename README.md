# portpinger
ICMP filtered? "Ping" a port instead.

Examples:
username@server:~$ ./portping.py dr.dk
Attempt 1: Time to connect to dr.dk:80 is 16.88ms
Attempt 2: Time to connect to dr.dk:80 is 10.77ms
Attempt 3: Time to connect to dr.dk:80 is 10.51ms
Attempt 4: Time to connect to dr.dk:80 is 7.68ms
Attempt 5: Time to connect to dr.dk:80 is 10.29ms

--- dr.dk port 80 connection statistics ---
5 connections, 5 successful, 0% failed, time 56.14 ms
rtt min/avg/max = 7.68/11.23/16.88 ms

username@server:~$ ./portping.py www.amazonaws.cn
Attempt 1: Time to connect to www.amazonaws.cn:80 is 165.82ms
Attempt 2: Time to connect to www.amazonaws.cn:80 is 146.63ms
Attempt 3: Time to connect to www.amazonaws.cn:80 is 168.23ms
Attempt 4: Time to connect to www.amazonaws.cn:80 is 199.46ms
Attempt 5: Time to connect to www.amazonaws.cn:80 is 223.75ms

--- www.amazonaws.cn port 80 connection statistics ---
5 connections, 5 successful, 0% failed, time 903.89 ms
rtt min/avg/max = 146.63/180.78/223.75 ms
