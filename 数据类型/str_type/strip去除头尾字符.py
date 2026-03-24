""" strip 去除头尾字符 """

# 初始字符内容
text: str = '\t-python '
print("初始字符内容：", text)

# 默认是去除首尾空白字符
print("去除首尾空白字符：", text.strip())

# 去除指定首尾字符（按字符集合匹配）
print("去除指定字符：", text.strip('\t-'))
