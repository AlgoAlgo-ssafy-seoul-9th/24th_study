import sys
input = sys.stdin.readline

N = int(input())
numbers = sorted(list(map(int, input().split())))

answer = [numbers[0], numbers[-1]]
sumV = abs(numbers[0] + numbers[-1])

left = 0
right = N - 1

while left < right:
    leftV = numbers[left]
    rightV = numbers[right]

    new_sum = leftV + rightV

    if abs(new_sum) < sumV:
        answer = [leftV, rightV]
        sumV = abs(new_sum)

        if new_sum == 0:
            break
    
    if new_sum < 0:
        left += 1
    else:
        right -= 1
    
print(*answer)

