class Solution {
    public int maxProfit(int[] prices) {
        int minp = prices[0];
        int answer = 0;

        for(int i=1; i<prices.length; i++) {
            minp = Math.min(minp, prices[i]);
            answer = Math.max(answer, prices[i] - minp);
        }

        return answer;
    }
}