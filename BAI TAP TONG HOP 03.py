#a
books=[{'name': 'Python Programming', 'code': 'PY123', 'num_page': 300, 'author': 'John Doe', 'type': 'Programming', 'descr': 'A comprehensive guide to Python programming.'}, 
       {'name': 'Machine Learning Basics', 'code': 'PY123', 'num_page': 250, 'author': 'John Doe', 'type': 'Machine Learning', 'descr': 'Introduction to machine learning concepts.'}, 
       {'name': 'Web Development with Django', 'code': 'WD789', 'num_page': 400, 'author': 'Alice Johnson', 'type': 'Web Development', 'descr': 'Learn Django framework for web development.'}, 
       {'name': 'Sci-Fi Adventure', 'code': 'SF001', 'num_page': 350, 'author': 'Michael Brown', 'type': 'Science Fiction', 'descr': 'Exciting sci-fi adventure novel.'}, 
       {'name': 'History of Art', 'code': 'HA567', 'num_page': 200, 'author': 'Emily White', 'type': 'Art', 'descr': 'Explore the history of art through the ages.'}]
# books=[]
# for i in range(5):
#     name = input("Tên sách: ")
#     code = input("Mã số sách: ")
#     num_page = int(input("Số trang sách: "))
#     author = input("Tác giả: ")
#     book_type = input("Thể loại: ")
#     descr = input("Mô tả: ")
    
#     book_info = {
#         'name': name,
#         'code': code,
#         'num_page': num_page,
#         'author': author,
#         'type': book_type,
#         'descr': descr
#     }
    
#     books.append(book_info)
# print(books)
#b
author_not_dup=set()
type_not_dup=set()
for i in books:
    if i['author'] not in author_not_dup:
        author_not_dup.add(i['author'])
print(*author_not_dup)
for i in books:
    if i['type'] not in type_not_dup:
        type_not_dup.add(i['type'])
print(*type_not_dup)
print()
#c
max_page=-10**18
min_page=10**18
for i in books:
    max_page=max(max_page,i['num_page'])
for j in books:
    min_page=min(min_page,j['num_page'])

for i in books:
    if i['num_page']==max_page:
        print(i['name'])
for i in books:
    if i['num_page']==min_page:
        print(i['name'])
print()
#d
d=dict({})
for i in books:
    if i['author'] in d:
        d[i['author']]+=1
    else:
        d[i['author']]=1
for x,y in d.items():
    if y>=2:
        print(x)
print()
#e
e=dict({})
for x in books:
    if x['code'] in e:
        e[x['code']]+=1
    else:
        e[x['code']]=1

def check_so(e):
    for x,y in e.items():
        if y<2:
            return False
    return True

print('yes') if check_so(e) else print('n')