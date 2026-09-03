class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        length = len(position)

        if length<=1:
            return length
        comb = []

        for i in range(len(position)):
            comb.append((position[i], speed[i]))
        
        comb.sort(reverse= True)

        #print("comb", comb)

        count = 1
        front_fleet = comb[0]
        front_time = (target - front_fleet[0])/front_fleet[1]
        i = 1

        while i < length:
            cur_car = comb[i]
            cur_time = (target - cur_car[0])/cur_car[1]
            #print("cur_car", cur_car, "cur_time",cur_time)
            #print("front_fleet", front_fleet, "front_time",front_time)
            if cur_time > front_time:
                #print("this run")
                front_fleet = cur_car
                front_time = cur_time
                count +=1
            i+=1
        return count

            
        