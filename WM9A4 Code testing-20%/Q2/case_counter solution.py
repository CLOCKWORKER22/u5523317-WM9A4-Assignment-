def case_counter(text):
    # 初始化计数器
    uppercase_count = 0
    lowercase_count = 0

    # 遍历字符串中的每个字符
    for char in text:
        # 检查字符是否为大写字母
        if char.isupper():
            uppercase_count += 1
        # 检查字符是否为小写字母
        elif char.islower():
            lowercase_count += 1

    # 返回结果
    return uppercase_count, lowercase_count

# 示例用法
text_example = "1234!@#$"
uppercase, lowercase = case_counter(text_example)
print(f"Uppercase letters: {uppercase}, Lowercase letters: {lowercase}")
