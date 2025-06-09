---
title: 数组
tags: [LeetCode, 数组]
categories: [Notes]
slug: 数组
publish: true
---
# 基础
【定义】存放在**连续内存空间**上的**相同类型**数据的集合。
【创建与寻址方法】
```cpp
// 创建 & 寻址
void creat_arr(){
	int array[2][3] = {
		{0, 1, 2},
		{3, 4, 5}
	};
		cout << &array[0][0] << " " << &array[0][1] << " " << &array[0][2] << endl;
		cout << &array[1][0] << " " << &array[1][1] << " " << &array[1][2] << endl;
int main(){
	test_arr();
    return 0;
}
/* 0x7ffee4065820 0x7ffee4065824 0x7ffee4065828
   0x7ffee406582c 0x7ffee4065830 0x7ffee4065834 */
   
// 索引 (以a*b维数组为例)
	array[0][1]
	array[0*a+1]
	*(&array + 0*a + 1) //*(内存地址+下标)
```

| Vector             |
| ------------------ |
| 底层实现是array，是容器而非数组 |
# 题目

## 二分查找
[704题](https://leetcode.cn/problems/binary-search/) [文章讲解](https://programmercarl.com/0704.%E4%BA%8C%E5%88%86%E6%9F%A5%E6%89%BE.html) [视频讲解](https://www.bilibili.com/video/BV1fA4y1o715)
【我的思路】只使用了middle和length（不断/2），于是struggle with奇偶/边界等问题。
【网站思路】贯彻左闭右闭/左闭右开；边界问题根据区间定义来；奇偶无所谓。
【代码】时间复杂度$O(logn)$, 空间$O(1)$
`有左闭右闭、左开右闭两种，这里是前者`
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0;
        int right = nums.size() - 1; 
        while (left <= right) { 
            int middle = left + ((right - left) / 2);// 防止溢出
            if (nums[middle] > target) {
                right = middle - 1; 
            } else if (nums[middle] < target) {
                left = middle + 1; 
            } else { // nums[middle] == target
                return middle;
            }
        }
        return -1;
    }
};
```

Optional: 搜索插入位置 (Optional) [35题]
Optional: 在排序数组中查找首/尾元素(Optional)[34题]

## 移除元素
[27题](https://leetcode.cn/problems/remove-element/) [文字讲解](https://programmercarl.com/0027.%E7%A7%BB%E9%99%A4%E5%85%83%E7%B4%A0.html) [视频讲解](https://www.bilibili.com/video/BV12A4y1Z7LP)
【我的思路】想法一是把后面的元素移到前面，难点在于保障copy到前面的不是targeted element；想法二是keep a set containing indexes of the targeted elements，然后新建一个array，把not in set的元素copy进去
- 思路1: T: $O(n^2)$  S: O(1)
```cpp
// copy自网站
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int size = nums.size();
        for (int i = 0; i < size; i++) {
            if (nums[i] == val) { // 发现需要移除的元素，就将数组集体向前移动一位
                for (int j = i + 1; j < size; j++) {
                    nums[j - 1] = nums[j];
                }
                i--; // 因为下标i以后的数值都向前移动了一位，所以i也向前移动一位
                size--; // 此时数组的大小-1
            }
        }
        return size;

    }
};
```
- 思路2: T: $O(n)$ S: $O(1)$
```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int last = nums.size() - 1;
        int k = nums.size();
        for (int i = 0; i <= last; i++){
            if (nums[i] == val){
                k -= 1;
                while (nums[last] == val && last > i){
                    last-= 1;
                    k -= 1;
                }
                if (last > i){
                    nums[i] = nums[last];
                    last -= 1;
                }
            }
        }
        return k;
    }
};
```
【网站思路】快慢指针法！只需要一个循环且思路简单，其中slow_ptr直接是s=新数组的size
T: $O(n)$ S: $O(1)$
`库函数erase是 $O(n)$`
```cpp
class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        int slow_ptr = 0;
        int fast_ptr = 0;
        for (;fast_ptr < nums.size(); fast_ptr++){
            if (nums[fast_ptr] != val){
                nums[slow_ptr++] = nums[fast_ptr];
            }
        }
        return slow_ptr;
    }
};
```
## 有序数组的平方
[977题](https://leetcode.cn/problems/squares-of-a-sorted-array/) [文章讲解](https://programmercarl.com/0977.%E6%9C%89%E5%BA%8F%E6%95%B0%E7%BB%84%E7%9A%84%E5%B9%B3%E6%96%B9.html) [视频讲解](https://www.bilibili.com/video/BV1QB4y1D7ep)
【我的思路】不知道如何排序，
【网站思路】平方后大的值在两端，所以想到双指针。可以把时间复杂度从O(n + nlog n)变成O(n)
- 暴力解法（copy from 网站）
```cpp
class Solution {
public:
    vector<int> sortedSquares(vector<int>& A) {
        for (int i = 0; i < A.size(); i++) {
            A[i] *= A[i];
        }
        sort(A.begin(), A.end()); // 快速排序
        return A;
    }
};
```
- 双指针解法
```cpp
class Solution {
public:
    vector<int> sortedSquares(vector<int>& nums) {
        vector<int> new_array(nums.size(),0);
        int k = nums.size() - 1;
        for (int i = 0, j = nums.size() - 1; i <= j;){ //注意是>=否则会漏掉
                if (nums[i]*nums[i] <= nums[j]*nums[j]){
                    new_array[k--] = nums[j] * nums[j];
                    j--;
                }else{
                    new_array[k--] = nums[i] * nums[i];
                    i++;
                }
        }
        return new_array;
    }
};
```

## 长度最小的子数组
[209题](https://leetcode.cn/problems/minimum-size-subarray-sum/)：
【题目】给定一个含有 n 个正整数的数组和一个正整数 s ，找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。如果不存在符合条件的子数组，返回 0。
【自己的思路：暴力搜索】 $O_t(n^2)$ , $O_s(1)$。用了两个for循环，遍历两次数组。这还导致了虽然测试用例都过了但Leetcode显示超时。
```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
    int length = nums.size();
    int min_length = length + 1;
    for(int i = 0; i < length; ++i){
        int cur_value = 0;
        int cur_length = 0;
        for(int j = i; j < length && cur_value < target; j++){
            cur_value += nums[j];
            cur_length++;
        }
        if (cur_length < min_length && cur_value >= target){min_length = cur_length;}
        }
    return min_length > length ？0 : min_length;
    }
    };
```

【随想录：滑动窗口（双指针）】$O_t(n)$ , $O_s(1)$。
```cpp
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
    int min_length = length + 1; //一个判断是否被改变 的技巧
    int cur_value = 0;
    int i = 0;
    int cur_length = 0;
    for (int j = 0;j < nums.size(); j++){
        cur_value += nums[j];
        while(cur_value >= target){
		    cur_length = j-i+1;
            min_length = cur_length < min_length ? cur_length : min_length;
            cur_value -= nums[i++];
        }
    }
    return min_length > length ? 0 : min_length;
    }
};
```

【关于数复杂度】不要单看循环的个数，这里要看每个元素被操作的次数：出去一次、进去一次——每个元素被操作两次，因此时间复杂度是2\*n。

```
🤔注：突发奇想打算把语言换成python
从下一道起就是Python啦
```
## 螺旋矩阵
给定一个正整数 n，生成一个包含 1 到 n^2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
[59题](https://leetcode.cn/problems/spiral-matrix-ii/)
【我的思路1】

【我的思路2】
设置一个储存的步长的array，每当“碰壁”就换一次方向，直到填满。
```python
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        array = [[0] * n for _ in range(n)]
        steps = [[0,1], [1,0], [0,-1], [-1, 0]]
        x, y = 0, 0
        num_change_dir = 0
        array[0][0] = 1
        for i in range(2, n**2 + 1):
            x_next = x + steps[num_change_dir][0]
            y_next = y + steps[num_change_dir][1]
            if ((x_next >= n) or (x_next < 0) or (y_next >= n) or (y_next < 0) or (array[x_next][y_next] != 0)):
                num_change_dir = (num_change_dir+1) % 4
            x_next = x + steps[num_change_dir][0]
            y_next = y + steps[num_change_dir][1]
            x, y = x_next, y_next
            array[x][y] = i
        return array
```

【语法[py_列表推公式](py_列表推公式.md)】
## 区间和
【[题目](https://kamacoder.com/problempage.php?pid=1070)】
【我的思路：分别累加】一行一行读取，进行累加。问题是超时，若查询次数为`m`，时间复杂度会变成 `O(n*m)`.
```python
def val_sum():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    while True:
        try:
            a, b = map(int, input().split())
        except:
            break
        print(sum(arr[a:b+1]))

if __name__ == "__main__":
    val_sum()
```

【随想录：前缀和】建立一个数组，记录累计的和。那么时间复杂度可以变成`O(n+m)`—— 这样就不需要每一次查询都累加一次。涉及计算区间和对问题时非常有效。
```python
def val_sum():
    n = int(input())
    arr = [int(input()) for _ in range(n)]
    # 创建“前缀和”array
    arr_acm = [arr[0]]
    for i in range(n - 1):
        arr_acm.append(arr_acm[i] + arr[i+1])
    # print结果
    while True:
        try: a, b = map(int, input().split())
        except: break # 没有输入时，结束
        if a == 0: print(arr_acm[b])
        else: print(arr_acm[b] - arr_acm[a-1])

if __name__ == "__main__":
    val_sum()
```
由于答案有用到`sys.stdin.read`，再写了一版
```python
import sys
def val_sum():
    txt = sys.stdin.readlines()
    n = int(txt[0])
    arr = [int(txt[i].strip()) for i in range(1, n+1)]
    arr_acm = [arr[0]]
    i = n + 1
    for j in range(n - 1):
        arr_acm.append(arr_acm[j] + arr[j+1])
    for i in range(n + 1, len(txt)):
        a, b = map(int, txt[i].split())
        if a == 0: print(arr_acm[b])
        else: print(arr_acm[b] - arr_acm[a-1])

if __name__ == "__main__":
    val_sum()
```
【语法：[_py_input](_py/_py_input.md)】
【语法：[_py_try_except](_py/_py_try_except.md)】
【语法：[_py_文件间运行](_py/_py_文件间运行.md)】

## 开发商购买土地
【[题目](https://kamacoder.com/problempage.php?pid=1044)】在一个 n $\times$ m 的区域内，每个区块有一个土地价值。需要将区域按**横向或纵向**划分为**两个子区域**，使得两个子区域内的土地总价值之差最小。
**输入格式**：第一行输入两个正整数 n 和 m。接下来 n 行，每行包含 m 个正整数，表示土地价值。
```
3 3
1 2 3
2 1 3
1 2 3
```
**输出格式**： 输出一个整数，表示两个子区域内土地总价值的最小差距。 `0`

【我的解法：优化暴力】$O_t(n*m)$。先算开发商分别有i和n-i排数据的情况，求差值的绝对值的最小值。再翻转矩阵重复此操作。问题是超出时间限制。
```python
def min_land_difference():
    # 计算整个区域的总价值
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(m)]
    total = sum(sum(row) for row in grid)
    min_diff = total
    # 横向切分：
    temp_sum = 0
    for i in range(n - 1): # 只考虑切分位置在前 n-1 行之后
        temp_sum += sum(grid[i])
        diff = abs(total - 2 * temp_sum)
        if diff < min_diff:
            min_diff = diff
    # 纵向切分：先转置
    temp_sum = 0
    transpose_grid = list(zip(*grid))
    for j in range(m - 1):
        temp_sum += sum(transpose_grid[j])
        diff = abs(total - 2 * temp_sum)
        if diff < min_diff:
            min_diff = diff
    print(min_diff)
# 示例测试
if __name__ == "__main__":
    min_land_difference() 
```

【随想录法一：前缀和】$O_t(n*m)$。
【随想录法二：暴力优化】$O_t(n*m)$。其实复杂度和我的一样，但没有用sum或者transpose的内置函数。莫名其妙时间就变少了？
【奇怪的发现：如果把我的解法所有 `sum()` 变成用循环自己求，那么时间就会大大减少，于是就通过了？但gpt说内置函数比自己写循环更快？不懂。
【语法：[_py_list](_py/_py_list.md)】

