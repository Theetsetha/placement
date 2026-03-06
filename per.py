if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    # 1. Get the list of scores for the specific student
    marks = student_marks[query_name]
    
    # 2. Calculate the average
    average = sum(marks) / len(marks)
    
    # 3. Format to 2 decimal places using f-string
    print(f"{average:.2f}")
