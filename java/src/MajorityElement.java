import  java.util.Map;
import java.util.HashMap;
public class MajorityElement {
    public int majorityElement(int[] nums) {
        int ans = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            map.put(nums[i], map.getOrDefault(nums[i], 0) + 1);
        }
        for (int i = 0; i < nums.length; i++) {
            if (map.get(nums[i]) > nums.length/2)
                ans = nums[i];
        }
        return ans;

    }
}
