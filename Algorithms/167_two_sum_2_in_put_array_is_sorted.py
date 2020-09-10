class Solution(object):
    def twoSum(self, numbers, target):
        new = list(set(numbers))
        run = 0
        for run in range(len(new)):
            init = new[run]
            init_index = numbers.index(init)
            makeup = target - init
            if init == makeup:
                if numbers.count(init) >= 2:
                    makeup_index = numbers[init_index+1:].index(makeup)+init_index+1
                    break
                else:
                    next
            else:
                if makeup in new:
                    makeup_index = numbers.index(makeup)
                    break
        if init_index > makeup_index:
            return [makeup_index+1, init_index+1]
        else:
            return [init_index+1, makeup_index+1]

