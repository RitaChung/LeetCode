class Solution(object):
    def intersect(self, nums1, nums2):
        num1 = {}
        for i in nums1:
            if i in num1.keys():
                num1[i] += 1
            else:
                num1[i] = 1
        num2 = {}
        for i in nums2:
            if i in num2.keys():
                num2[i] += 1
            else:
                num2[i] = 1
        elms = set(num1.keys()).intersection(set(num2.keys()))
        result = []
        for elm in elms:
            if num1[elm] < num2[elm]:
                for i in range(num1[elm]):
                    result.append(elm)
            else:
                for i in range(num2[elm]):
                    result.append(elm)
        return result

