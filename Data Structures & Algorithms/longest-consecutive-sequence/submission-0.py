class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        
        newNums = set(nums)
        dic = {}
        minmax = {}
        maxmin ={}

        max_len = 1 
        
        for num in newNums:
            if num+1 in minmax and num-1 in maxmin:
                newMax = minmax[num+1]
                newMin = maxmin[num-1]
                pre = dic[(maxmin[num-1], num-1)]
                sur = dic[(num+1, minmax[num+1])]
                dic[(newMin, newMax)] = pre + [num] + sur  
                del minmax[num+1], maxmin[num-1]
                minmax[newMin] = newMax
                maxmin[newMax] = newMin

                if len(dic[(newMin, newMax)]) > max_len:
                    max_len = len(dic[(newMin, newMax)])

            else:
                # Num become the new min
                if num+1 in minmax:
                    originMax = minmax[num+1]
                    dic[(num+1), originMax].append(num)
                    dic[(num, originMax)] = dic[(num+1, originMax)]
                    del dic[(num+1, originMax)]
                    del minmax[num+1]
                    minmax[num] = originMax
                    maxmin[originMax] = num

                    if len( dic[(num, originMax)]) > max_len:
                        max_len = len( dic[(num, originMax)])
                
                # Num become the new max
                elif num-1 in maxmin:
                    originMin = maxmin[num-1]
                    dic[(originMin, num-1)].append(num)
                    dic[(originMin, num)] = dic[(originMin, num-1)]
                    del dic[(originMin, num-1)]
                    del maxmin[num-1]
                    maxmin[num] = originMin
                    minmax[originMin] = num
                    if len(dic[(originMin, num)]) > max_len:
                        max_len = len( dic[(originMin, num)])

                else:
                    dic[(num,num)] = [num]
                    minmax[num] = num
                    maxmin[num] = num

        return max_len