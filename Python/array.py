# 配列

# 宣言+初期化（空）
list = []

# print(list[0]) IndexError

# 宣言+初期化
list2 = [1, 2, 3]
print(list2[0]) # 1
print(list2[1]) # 2
print(list2[2]) # 3

# 配列末尾に追加
list2.append(4)
print(list2) # [1, 2, 3, 4]

# 配列末尾に追加
list2 += [5]
print(list2) # [1, 2, 3, 4, 5]

# 要素の挿入
# insert(挿入する位置, 挿入する値)
list2.insert(3, 6)
print(list2) # [1, 2, 3, 6, 4, 5]

# 要素の削除（添え字指定）
del list2[2]
print(list2) # [1, 2, 6, 4, 5]

# 要素の削除（インデックス指定）
list2.pop(0)
print(list2) # [2, 6, 4, 5]

# 要素の削除（値指定）
list2.remove(4)
print(list2) # [2, 6, 5]

# 配列の長さ
print(len(list2)) # 3
