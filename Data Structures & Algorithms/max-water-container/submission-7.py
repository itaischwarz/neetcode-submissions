class Solution:
    def maxArea(self, heights: List[int]) -> int:
        def compute_area(x1, x2):
            return (x2 - x1) *  min(heights[x1], heights[x2])
        x1 = 0
        x2 = len(heights)-1
        max_area = 0
        while x1 != x2:
            compute = compute_area(x1, x2)
            max_area = max(compute, max_area)
            if heights[x1] >= heights[x2]:
                x2-=1
            else:
                x1+=1
        return max_area

        