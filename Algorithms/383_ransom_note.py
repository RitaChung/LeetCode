class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        length = len(ransomNote)
        if length == 0:
            return True

        ran_dic = {}
        for chr in ransomNote:
            if chr not in ran_dic.keys():
                ran_dic[chr] = 1
            else:
                ran_dic[chr] += 1

        mag_dic = {}
        for chr in magazine:
            if chr not in mag_dic.keys():
                mag_dic[chr] = 1
            else:
                mag_dic[chr] += 1

        for item in ran_dic.keys():
            if item not in mag_dic.keys():
                return False
            else:
                if mag_dic[item] < ran_dic[item]:
                    return False
        return True
