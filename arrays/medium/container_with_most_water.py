"""

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # area to be returned
        area = 0

        # two pointers
        i, j = 0, len(height) - 1

        # while the start pointer is less and the end one
        while i < j:
            # get new height and width to calculate new area
            new_area_height = min(height[i], height[j])
            new_area_width = j - i
            new_area = new_area_height * new_area_width

            # assign the maximum in comparison to the previous area
            area = max(new_area, area)

            # shift pointers depending on which height is lower
            if height[i] < height[j] or height[j] == height[i]:
                i +=1
            else:
                j-=1
        
        return area

print(Solution.maxArea(Solution, [1,8,6,2,5,4,8,3,7]))


