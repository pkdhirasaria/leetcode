class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        	int n=nums.size(), max=-100000, sum=0;
	for(int i=0; i<n; i++){
		if(sum>=0)
			sum+=nums[i];
		else if(sum<0)
			sum=nums[i];
		if(max<sum)
			max=sum;
	}
	return max;

    }
};