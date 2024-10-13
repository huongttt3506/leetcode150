public class RomanToInteger {
    public int romanToInt(String s) {
        int answer = 0;
        for (int i = 0; i < s.length(); i++) {
            switch (s.charAt(i)){
                case 'I' : answer += 1;break;
                case 'V': answer += 5;break;
                case 'X' : answer +=10;break;
                case 'L' : answer +=50;break;
                case 'C': answer +=100;break;
                case 'D': answer +=500;break;
                case 'M': answer += 1000;break;
            }
        }
        if(s.contains("IV")) answer -=2;
        if(s.contains("IX")) answer -=2;
        if (s.contains("XL")) answer -=20;
        if (s.contains("XC")) answer -=20;
        if (s.contains("CD")) answer -=200;
        if (s.contains("CM")) answer -=200;

        return answer;
    }
}
