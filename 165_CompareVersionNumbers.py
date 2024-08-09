class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        ldiff = len(v1) - len(v2)
        if ldiff > 0:
            v2 += ["0"] * ldiff
        else:
            v1 += ["0"] * abs(ldiff)
        for i in range(len(v1)):
            if int(v1[i]) > int(v2[i]):
                return 1
            elif int(v1[i]) < int(v2[i]):
                return -1
        return 0
