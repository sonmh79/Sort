class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        # 첫번째 원소 기준으로 정렬
        for i in sorted(intervals, key = lambda x: x[0]):
            # 겹치게 된다면 병합
            if merge and i[0] <= merge[-1][1]:
                merge[-1][1] = max(i[1], merge[-1][1])
            else:
                # 쉼표를 사용해서 리스트 형태로 추가
                merge += i,
        return merge
        
        
