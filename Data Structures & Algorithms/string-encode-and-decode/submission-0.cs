public class Solution {

    public string Encode(IList<string> strs) {
        StringBuilder encode = new StringBuilder();

        foreach (string s in strs) {
            encode.Append(s.Length);
            encode.Append('#');
            encode.Append(s);
        }
        return encode.ToString();
    }

    public List<string> Decode(string s) {
        List<string> decode = new List<string>();
        int i = 0;
        while (i < s.Length) {
            int j = i;

            while (s[j] != '#') j++;

            int dodai = int.Parse(s.Substring(i, j - i));
            string kitu = s.Substring(j + 1, dodai);

            decode.Add(kitu);

            i = j + 1 + dodai;
        }
        return decode;
   }
}
