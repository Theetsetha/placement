if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])

    # 1. Get unique scores and sort them to find the second lowest
    unique_scores = sorted(list(set(score for name, score in students)))
    second_lowest_score = unique_scores[1]

    # 2. Collect names of students with that score
    names = [name for name, score in students if score == second_lowest_score]

    # 3. Sort names alphabetically and print
    for name in sorted(names):
        print(name)
