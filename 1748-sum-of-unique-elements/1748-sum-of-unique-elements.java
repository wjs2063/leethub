class Solution {
    public int sumOfUnique(int[] nums) {
        Map <Integer,Integer> counter = new HashMap<>();
        
        for (int i : nums){
            if (counter.containsKey(i))counter.put(i,counter.get(i) + 1);
            else{
                counter.put(i,1);
            }
        }
        int res = 0;
        for (int i : counter.keySet()){
            if (counter.get(i) == 1) res += i;
        }
        
        return res;
        
    }
}