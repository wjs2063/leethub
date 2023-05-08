class Solution {
    public int countMatches(List<List<String>> items, String ruleKey, String ruleValue) {
        int idx = 0;
        
        if (ruleKey.equals("color")) idx = 1;
        if (ruleKey.equals("name")) idx = 2;
        
        int res = 0;
        int n = items.size();
        for (int i = 0; i < n;i++){
            if (items.get(i).get(idx).equals(ruleValue)){
                res ++;
            }
        }
        return res;
        
    }
}