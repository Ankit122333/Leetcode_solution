class Solution {
    public int minimumSum(int num) {
        int[] arr = new int[4];
        int m =0;
        while(num>0)
        {
            arr[m] = num%10;
            num = num/10;
            m++;
        }
        Arrays.sort(arr);
        int a = arr[0]*10+arr[3];
        int b = arr[1]*10+arr[2];
        System.out.println(b);
        System.out.println(b);
        return (a+b);
        
    }
}