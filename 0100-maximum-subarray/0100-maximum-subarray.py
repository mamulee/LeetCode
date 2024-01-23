class Solution:
    # @param A, a list of integers
    # @return an integer
    def maxSubArray(self, A):
        sum = [0]*len(A)
        sum[0] = A[0]
        if len(A)==1:
            return A[0]

        max = -sys.maxint-1
        for i in range(1,len(A)):
            if sum[i-1]>0:
                sum[i]=sum[i-1]+A[i]
                if sum[i]>max:
                    max = sum[i]
            if sum[i-1]<0:
                sum[i]=A[i]
                if sum[i]>max:
                    max = sum[i]
        return max