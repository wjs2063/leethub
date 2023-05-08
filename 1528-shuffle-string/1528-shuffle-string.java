class Solution {
    public String restoreString(String s, int[] indices) {
        int n = s.length();
        String [] arr = new String[n];
        String res ;
        for (int i = 0;i < n;i++){
            arr[indices[i]] = String.valueOf(s.charAt(i));
        }
        res = String.join("",arr);
        return res;
        
        
    }
}