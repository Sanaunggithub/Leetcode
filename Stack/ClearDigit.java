class Solution {
    public String clearDigits(String s) {
        Stack<Character> s1 = new Stack<Character>();

        for (int i = 0; i < s.length(); i++){
            if(Character.isDigit(s.charAt(i))){
                s1.pop();
            } else{
                s1.push(s.charAt(i));
            }
        }

        StringBuilder sb = new StringBuilder();
        for (char c : s1) {
            sb.append(c);
        }
        return sb.toString();

    }
}