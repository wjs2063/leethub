class Solution {
    public int countPoints(String rings) {
        
        Map <Character,Set<Character>> hash = new HashMap<>();
        int n = rings.length();
        int i = 0;
        while (i < n ){
            if (hash.get(rings.charAt(i + 1)) == null){
                hash.put(rings.charAt(i + 1),new HashSet<Character>());
                hash.get(rings.charAt(i + 1)).add(rings.charAt(i));
            }
            else{
                hash.get(rings.charAt(i + 1)).add(rings.charAt(i));
            }
            i += 2;
            
        }
        int res = 0;
        for (Set<Character> s : hash.values()){
            if (s.size() == 3) res ++;
        }
        return res;
    }
    
}