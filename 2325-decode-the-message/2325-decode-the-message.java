class Solution {
    public String decodeMessage(String key, String message) {
        String replace_key = key.replaceAll(" ","");
        StringBuilder s = new StringBuilder();
        int n = replace_key.length();
        int asc = (int)('a');
        HashMap <Character,Character> hash = new HashMap<>();
        int inc = 0;
        for (int i = 0;i < n;i++){
            if (hash.containsKey(replace_key.charAt(i))) continue;
            hash.put(replace_key.charAt(i),(char)(asc + inc));
            inc++;
            //System.out.println(replace_key.charAt(i) + " " + (char)(asc + i));
        }
        int msg_len = message.length();
        
        for (int i = 0 ;i < msg_len;i++){
            if (message.charAt(i) == ' ')s.append(" ");
            else {
                s.append(hash.get(message.charAt(i)));
            }
        }
        return s.toString();
    }
}