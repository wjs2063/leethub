class Solution {
    public String sortSentence(String s) {
        
        String [] split_str = s.split(" ");
        int n = split_str.length;
        String [] arr = new String[n];
        for (String wo:split_str){
            int last_idx = Character.getNumericValue(wo.charAt(wo.length() - 1));
            arr[last_idx - 1] = wo.substring(0,wo.length() - 1);
        }
        String res = String.join(" ",arr);
        return res;
    }
}