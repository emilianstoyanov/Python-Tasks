import ipaddress


def solution(inputString):
    try:
        ipaddress.ip_address(inputString)
    except:
        return False
    return True


print(solution("172.16.254.1"))
# True
