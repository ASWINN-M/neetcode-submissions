class Solution {
    public int[] maxSlidingWindow(int[] nums, int k) {
        int l , r;
        l = 0;
        r = 0;
        ArrayList<Integer> res = new ArrayList<>();
        Deque<Integer> q = new LinkedList<>();

        while(r < nums.length){
            while(!q.isEmpty() && nums[q.peekLast()] < nums[r]){
                q.pollLast();
            }
            q.add(r);

            if(l > q.peekFirst()){
                q.pollFirst();
            }

            if(r >= k - 1){
                res.add(nums[q.peekFirst()]);
                l ++;
            }
            r++;
        }
        int[] ans = new int[res.size()];

        for (int i = 0; i < res.size(); i++) {
            ans[i] = res.get(i);
        }

        return ans;
    }
}
