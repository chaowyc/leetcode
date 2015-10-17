### move zeros
### 题意
给一个数组，将数组里面全部的0放到数组末尾，其他非零元素相对位置保持不变。
### 题解
设两个指针，一个指针p指向当前扫描的位置，一个指针q是当前应该存储的位置
当p扫描到非零元素时 把此位置上的值赋给q所指向的位置，同时q向前移动
当p扫描到零元素时，略过，直到再次找非零元素位置。
代码如下：

    void moveZeroes(int* nums, int numsSize) {
    	int p = 0;
    	for(int i = 0; i < numsSize; i++)
    	{
        	if(nums[i] != 0)
       		{
            	nums[p] = nums[i];
            	p++;
        	}
    	}
    	for(int i = p; i < numsSize; i++)
    	{
        	nums[i] = 0;
    	}
	}
