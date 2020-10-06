import java.util.ArrayList;

class Solution {
    public boolean isAnagram() {
        String s="anagram";
        String t="nagaram";
        ArrayList<Character> slist = new ArrayList<Character>();
        for(char ch:s.toCharArray())
        {
            slist.add(ch);         
        }
        for(char ch:s.toCharArray())
        {
            if(s.length()==t.length())
                
                
            else if(slist.contains(ch)==false)
                return false;
        }
        return true;
    }
}
}