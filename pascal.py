"""
Copyright MIT BWSI Autonomous RACECAR Course
MIT License
Summer 2022

Code Clash #17 - Pascal's Triangle (pascal.py)


Author: Paul Thai

Difficulty Level: 6/10

Background: Blaise Pascal is a famous French Mathematician and Philosopher who 
created Pascal's Triangle. Pascal's Triangle is a triangular array composed of 
binomial coefficients that arises in probability theory, combinatorics, and algebra. (Wikipedia)

Prompt: Given the number of rows, return a 2D list of Pascal's Triangle

Test Cases:
Input: rows = 1 ; Output = [[1]]
Input: rows = 2 ; Output = [[1], [1, 1]]
Input: rows = 3 ; Output = [[1], [1, 1], [1, 2, 1]]

"""

class Solution:
    def pascalTri(self,rows):
        # type row: int
        # return type: list[list[int]]

        # TODO: Write code below to return a nested list with the solution to the prompt
        # list = [] 
        # for n in range(rows):
        #     list.append([])
        #     list[n].append(1)
        #     for m in range(1, n):
        #         list[n].append(list[n - 1][m - 1] + list[n - 1][m])
        #     if(rows != 0):
        #         list[n].append(1)
        # res = []
        # for n in range(rows):
        #     t = []
        #     for m in range(0, n + 1):
        #         t.append(list)
        #     res.append(t)
        # return res
        res = []
        for n in range(1, rows+1):  
            for m in range(0, rows-n+1):  
                print(' ', end='')  
            B = 1  
            t = []
            for m in range(1, rows+1):  
                if B!=0:
                    t.append(B)
                B = B * (n - m) // m 
            res.append(t)
        return res

def main():
    num = int(input())

    tc1 = Solution()
    ans = tc1.pascalTri(num)
    print(ans)

if __name__ == "__main__":
    main()