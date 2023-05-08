class Solution {
    public boolean checkIfPangram(String sentence) {
        
        int n = sentence.length();
        HashSet <Character> alphabet = new HashSet<>();
        
        for (int i = 0;i < n;i++){
            alphabet.add(sentence.charAt(i));
        }
        
        return alphabet.size() == 26;
        
    }
}