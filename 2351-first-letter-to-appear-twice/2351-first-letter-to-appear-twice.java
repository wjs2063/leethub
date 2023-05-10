class Solution {
    public char repeatedCharacter(String s) {
        Map <String,Integer> counter = new HashMap<>();
        char ans = '1' ;
        for (String w : s.split("") ){
            if (counter.containsKey(w)){
                counter.put(w,counter.get(w) + 1);
            }
            else{
                counter.put(w,1);
            }
            
            if (counter.get(w) == 2){
                ans = w.charAt(0);
                break;
            }
            
        }
        return ans;
    }
}