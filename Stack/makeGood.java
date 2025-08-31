public String makeGood(String s) {
    Stack<Character> stack = new Stack<>(); 
    char ch, tmp = '/'; 
    for (int i = 0; i < s.length(); i++) { 
        ch = s.charAt(i); 
        if (stack.isEmpty()) { 
            stack.push(ch); 
            continue; 
        }

        tmp = stack.peek(); 
        if (Math.abs(tmp - ch) == 32) { 
            stack.pop(); 
            continue; 
            
        } 
        stack.push(ch); 
    } 
    StringBuilder sb = new StringBuilder(); 
    while (!stack.isEmpty()) { 
        sb.append(stack.pop()); 
        } 
    return sb.reverse().toString(); 
}