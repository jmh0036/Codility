def solution(S):
    openings = []
    for i in S:
        if i in {'{','[','('}:
            openings.append(i)
        elif openings == []:
            return 0
        elif i == '}' and openings.pop() != '{':
            return 0
        elif i == ']' and openings.pop() != '[':
            return 0
        elif i == ')' and openings.pop() != '(':
            return 0
    if openings == []:
        return 1
    else:
        return 0
                
print(solution('{[()()]}'))