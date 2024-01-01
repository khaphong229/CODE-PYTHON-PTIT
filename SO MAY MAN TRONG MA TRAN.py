def find_lucky_number(matrix):
    n = len(matrix)
    m = len(matrix[0])

    max_value = float('-inf')
    min_value = float('inf')

    # Tìm giá trị lớn nhất và nhỏ nhất trong ma trận
    for i in range(n):
        for j in range(m):
            max_value = max(max_value, matrix[i][j])
            min_value = min(min_value, matrix[i][j])

    lucky_number = max_value - min_value

    # Kiểm tra và in ra vị trí nếu tìm thấy số may mắn
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == lucky_number:
                print(lucky_number)
                print(f"Vi tri [{i}][{j}]")
                return

    # In ra NOT FOUND nếu không tìm thấy số may mắn
    print("NOT FOUND")

# Đọc input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Gọi hàm để tìm số may mắn và vị trí
find_lucky_number(matrix)
