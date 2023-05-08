class Solution {
    public String interpret(String command) {
        int n = command.length();
        int idx = 0;
        StringBuilder res = new StringBuilder();
        System.out.println(command.charAt(0));
        while (idx < n){
            if (command.charAt(idx) == '(') {
                if (command.charAt(idx + 1) == ')') {
                    res.append("o");
                    idx += 2;
                    continue;
                }
                else {
                    idx += 1;
                    continue;
                }
            }
            else if (command.charAt(idx) == ')') {
                idx += 1;   
            }
            else{
                res.append(command.charAt(idx));
                idx += 1;
            }
        }
        return res.toString();
    }
}