""" 英文字符大小写转换 """

# 初始字符内容
text: str = "hello Word"
print("初始字符内容：", text)

# 全转换为大写
print("全转换为大写：", text.upper())

# 全转换为小写
print("全转换为小写：", text.lower())

# 大小写互转换
print("大小写互转换：", text.swapcase())

# 转换为标题字（单词首字母大写）
print("转换为标题字：", text.title())

# 句首字母大写
print("句首字母大写：", text.capitalize())
