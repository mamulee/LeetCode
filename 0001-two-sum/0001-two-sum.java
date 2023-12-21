class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[] answer = new int[2]; // O(1)
        HashMap<Integer, Integer> hm = new HashMap<>(); // O(1)
        int pair = 0; // O(1)
        for(int i=0; i < nums.length; i++) { // O(n)
            pair = target - nums[i]; // O(1)
            if(hm.containsKey(pair)) { // O(1)
                answer[0] = i; // O(1)
                answer[1] = hm.get(pair); // O(1)
            }
            hm.put(nums[i], i); // O(1)
        }

        return answer;
    }
}

// time : O(n)
// space : O(n)