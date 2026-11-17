class Solution:
    def paint(self, A: int, B: int, C: list[int]) -> int:
        MOD = 10000003
        left = max(C)
        right = sum(C)
        while left <= right:
            mid = (left + right) >> 1
            painters_needed = self.count_painters(C, mid)
            if painters_needed > A:
                left = mid + 1
            else:
                right = mid - 1
        return (left * B) % MOD

    def count_painters(self, boards: list[int], max_units: int) -> int:
        painters = 1
        current_units = 0
        for board in boards:
            if current_units + board <= max_units:
                current_units += board
            else:
                painters += 1
                current_units = board       
        return painters
