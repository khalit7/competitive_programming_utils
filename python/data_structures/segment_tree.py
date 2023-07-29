class SegmentTree:
    # index zero is not included in segment tree for simplicity
    def init(self,function):
        self.function=(lambda x,y:x+y) if function==sum else function
        self.fill_value = float("inf") if function == min else (float("-inf") if function==max else 0)
    def construct(self,array):
        n=len(array)
        array+=[self.fill_value]*((1<<((n-1).bit_length()))-n)
        self.n=len(array)
        self.segment_tree = [0] * (self.n << 1)
        for i in range(self.n):
            self.segment_tree[i + self.n] = array[i]
        for i in range(self.n - 1, 0, -1):
            self.segment_tree[i] = self.function(self.segment_tree[i << 1],self.segment_tree[i << 1 | 1])

    def update(self,index,value):
        index += self.n
        self.segment_tree[index] = value
        while (index > 1):
            self.segment_tree[index >> 1] = self.function(self.segment_tree[index],self.segment_tree[index ^ 1])
            index >>= 1

    def query(self,left_bound,right_bound):
        # left bound and right bound are inclusive
        left_bound += self.n
        right_bound += self.n
        ans = self.fill_value
        while (left_bound <= right_bound):
            if (left_bound & 1):  # right child
                ans = self.function(ans,self.segment_tree[left_bound])
                left_bound += 1
            if (not (right_bound & 1)):
                ans = self.function(ans, self.segment_tree[right_bound])
                right_bound -= 1
            left_bound >>= 1
            right_bound >>= 1
        return ans