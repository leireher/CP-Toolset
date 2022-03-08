import java.util.*;

public class KMP {
    
    public final String p;
    private final int[] b;
    
    public KMP(String p) {
        this.p = p; this.b = new int[p.length()+1];
        int i = 0, j = -1; b[0] = -1; // starting values
        while (i < p.length()) { // pre-process the pattern string p
            while (j >= 0 && p.charAt(i) != p.charAt(j)) j = b[j]; // if different, reset j using b
            i++; j++; // if same, advance both pointers
            b[i] = j;
        }
    }
    
    public List<Integer> searchAt(String s) {
        final List<Integer> res = new ArrayList<Integer>();
        int i = 0, j = 0; // starting values
        while (i < s.length()) { // search through string s
            while (j >= 0 && s.charAt(i) != p.charAt(j)) j = b[j]; // if different, reset j using b
            i++; j++; // if same, advance both pointers
            if (j == p.length()) { // a match found when j == p.length
                res.add(i-j);
                j = b[j]; // prepare j for the next possible match
            }
        }
        return res;
    }
    
}
