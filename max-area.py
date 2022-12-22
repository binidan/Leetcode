def maxArea(height: list[int]):
        area = 0
        l = len(height)
        for i in range(l):
            for j in range(i+1, l):
                area = max(area, min(height[i], height[j])*(j-i))

        return area

height = [1,8,6,2,5,4,8,3,7]
print(maxArea(height))

