class Solution {
    public int minimumCost(int[] cost) {
        int n=cost.length, ans=0;
        Arrays.sort(cost);
        int i = n-1;
        while(i>=0)
        {
            if(i>=0)
            {
                ans+=cost[i];
            }
            i--;
            if(i>=0)
            {
                ans+=cost[i];
            }
            i--;
            i--;
        }
        return ans;
        
    }
}