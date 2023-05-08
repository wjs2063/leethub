class Solution {
    public int firstUniqChar(String s) {
        Map <String,Integer> counter = new HashMap<>();
        
        for (String str : s.split("")){
            if (counter.containsKey(str)){
                counter.put(str,counter.get(str) + 1);
            }
            else{
                counter.put(str,1);
            }
        }
        for (int i = 0;i < s.length();i++){
            String temp = Character.toString(s.charAt(i));
            if (counter.get(temp) == 1){
                return i;
            }
        }
        return -1;
    }
}