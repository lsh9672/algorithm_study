import sys

n = int(sys.stdin.readline().strip())

book = dict()

for _ in range(n):
    book_name = sys.stdin.readline().strip()

    if book_name in book:
        book[book_name] += 1
    
    else:
        book[book_name] = 1

result = list(book.items())

result.sort(key=lambda x : [-x[1],x[0]])

print(result[0][0])