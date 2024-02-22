def solution(numbers):
    answer = ''        
    numbers.sort(key = lambda x : x*10, reverse=True)
    answer = ''.join(numbers)
    
    return answer

n = int(input())
arr = [input() for _ in range(n)]
print(solution(arr))