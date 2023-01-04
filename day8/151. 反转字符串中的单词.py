# -*- coding: utf-8 -*-            
# @Time : 2023/1/4 19:59
# @Author: zouying
# @FileName: 151. 反转字符串中的单词.py
# @Software: PyCharm
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        remove_slist = []
        lindex = 0
        while slist[lindex]==' ':
            lindex += 1
        rindex = len(slist)-1
        while slist[rindex] == ' ':
            rindex -= 1
        remove_slist = slist[lindex:rindex+1]
        length = len(remove_slist)
        index = 0
        while index < length:
            if remove_slist[index]==' ' and remove_slist[index-1] == ' ':
                remove_slist = remove_slist[: index]+remove_slist[index+1:]
                length -= 1
                index -= 1
            index += 1
        # 反转整个字符串
        left = 0
        right = len(remove_slist) - 1
        while left < right:
            remove_slist[left], remove_slist[right] = remove_slist[right], remove_slist[left]
            left += 1
            right -= 1
        # 反转单词
        left = 0
        for index in range(0, len(remove_slist)):
            if remove_slist[index] == ' ':
                right = index - 1
                while left < right:
                    remove_slist[left], remove_slist[right] = remove_slist[right], remove_slist[left]
                    left += 1
                    right -= 1
                left = index + 1
        right = len(remove_slist)-1
        while left < right:
            remove_slist[left], remove_slist[right] = remove_slist[right], remove_slist[left]
            left += 1
            right -= 1
        return ''.join(remove_slist)
    def reverseWords1(self, s):
        """
        :type s: str
        :rtype: str
        """
        slist = list(s)
        wordlist = []
        word = ''
        for i in slist:
            if i != ' ':
                word += i
            if i == ' ':
                if word != '':
                    wordlist.append(word)
                word = ''
        if word != '':
            wordlist.append(word)
        news = wordlist[len(wordlist)-1]
        for index in range(len(wordlist)-2, -1, -1):
            if wordlist[index] !=' ' :
                news += (' '+wordlist[index])
        return news

if __name__ == '__main__':
    solution = Solution
    print(solution.reverseWords(solution, "  hello    world  "))