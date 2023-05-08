class Solution {
    public String[] sortPeople(String[] names, int[] heights) {
        HashMap <Integer,String> hash = new HashMap<>();
        String [] res = new String [heights.length];
        for (int i = 0;i < heights.length;i++){
            hash.put(heights[i],names[i]);
        }
        
        Arrays.sort(heights);
        
        for (int i = heights.length - 1 ;i >= 0 ;i--){
            res[heights.length - 1 - i] = hash.get(heights[i]);
        }
        return res;
    }
}