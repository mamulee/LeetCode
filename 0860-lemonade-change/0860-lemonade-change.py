class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five_bill_count = 0
        ten_bill_count = 0

        for bill in bills:
            if bill == 5:
                five_bill_count += 1
            elif bill == 10:
                if five_bill_count > 0:
                    five_bill_count -= 1
                    ten_bill_count += 1
                else:
                    return False
            elif bill == 20:
                if ten_bill_count > 0 and five_bill_count > 0:
                    ten_bill_count -= 1
                    five_bill_count -= 1
                elif five_bill_count >= 3:
                    five_bill_count -= 3
                else:
                    return False

        return True