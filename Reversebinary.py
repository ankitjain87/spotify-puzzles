
N = int(raw_input())
binary_no = bin(N)
reverse = binary_no[:1:-1]
print int(reverse, 2)

"""This can be also be done in one line, its just for code readability."""

# print int(bin(int(raw_input()))[:1:-1], 2)
