class Solution {
    public String reversePrefix(String word, char ch) {
        int n = word.length();
        int idx = -1;
        for (int i = 0;i < n;i++){
            if (word.charAt(i) == ch){
                idx = i;
                break;
            }
        }
        StringBuilder s = new StringBuilder();
        if (idx == -1) return word;
        for (int i = idx;i >= 0;i--){
            s.append(word.charAt(i));
        }
        for (int i = idx + 1;i < n;i++){
            s.append(word.charAt(i));
        }
        return s.toString();
    }
}