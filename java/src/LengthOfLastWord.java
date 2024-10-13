public class LengthOfLastWord {
    public int lengthOfLastWord(String s) {
        String[] s_splited = s.split(" ");
        String lastWord = s_splited[s_splited.length -1];
        return lastWord.length();

    }
}
