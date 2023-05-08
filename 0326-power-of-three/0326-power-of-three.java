class Solution {
    public boolean isPowerOfThree(int n) {
        return solve(n);
    }
    
    
    public boolean solve(int n ){
        if (n <= 0) return false;
        
        while (n > 1){
            if (n % 3 == 0 ){
                n /= 3;
            }
            else{
                return false;
            }
        }
        return true;
    }
}