#Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

def ips_between(start, end):
    start = start.split('.'); start = list(map(int, start))
    end = end.split('.'); end = list(map(int, end))
    a = 16777216; b = 65536; c = 256; d = 1
    
    ips = 0
    ips += (end[3] - start[3])
    ips += ((end[2] * c) - (start[2] * c))
    ips += ((end[1] * b) - (start[1] * b))
    ips += ((end[0] * a) - (start[0] * a))
    return ips
