// Given a string s, return the last substring of s in lexicographical order.

 

// Example 1:

// Input: s = "abab"
// Output: "bab"
// Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"].
// The lexicographically maximum substring is "bab".
// Example 2:

// Input: s = "leetcode"
// Output: "tcode"
 

// Constraints:

// 1 <= s.length <= 4 * 105
// s contains only lowercase English letters.

// 这题的意思是：找到最长的substring，是按字典顺序的。比如说aba 比 bcb小，因为第一个字母，b比a大
// 所以用两个指针，分别比较当前数字大小，如果一样大，那么用另一个var来开始分别走他们后面的substirng
// 比如说，现在i j都是a，然后用一个k来代表现在i j 后面的位置，i+0, j+0, i+1, j+1之类的往后走，
// 比较当前两个数字。如果碰到了i比较大，那么j继续走，如果j比较大，那么移动i。

var lastSubstring = function (s) {
  let i = 0,
    j = 1,
    k = 0;
  while (j + k < s.length) {
    if (s[i + k] === s[j + k]) {
      k++;  // 比较substirng的字母
      continue;
    } else if (s[i + k] > s[j + k]) {
      j = j + k + 1;  // 移动j 
    } else {
      i = Math.max(j, i + k + 1);  // 不是很明白这里
      j = i + 1;
    }
    k = 0;
  }
  return s.slice(i);
};