import os

# 准备一个文件名
filename = "example.txt"

# 1. 创建并写入文件
# 使用 'w' 模式打开会创建文件（如果不存在），并清空文件内容（如果已存在）
with open(filename, 'w', encoding='utf-8') as f:
    f.write("Hello, world!\n")
    f.write("This is a sample file.\n")
    # 写入多行字符串
    lines = ["Python file handling is simple.\n", "End of file.\n"]
    f.writelines(lines)

print(f"File '{filename}' created and data written.")

# 2. 读取文件内容
# 使用 'r' 模式进行只读打开（默认模式也是 'r'）
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()  # 一次性读取整个文件内容到字符串
    print("File content (read all at once):")
    print(content)

# 3. 逐行读取文件
with open(filename, 'r', encoding='utf-8') as f:
    print("Reading file line by line:")
    for line in f:
        print(repr(line))  # 使用repr()来显示换行符等特殊字符

# 4. 使用 readlines() 将文件内容读入列表
with open(filename, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    print("File content as list:")
    print(lines)

# 5. 追加写入文件 ('a' 模式)
# 使用 'a' 模式打开文件，会在文件末尾添加新内容，而不清空原文件
with open(filename, 'a', encoding='utf-8') as f:
    f.write("Appending a new line at the end.\n")

# 验证是否追加成功
with open(filename, 'r', encoding='utf-8') as f:
    print("File content after append:")
    print(f.read())

# 6. 使用 'x' 模式创建文件，如果文件已存在会报错，避免覆盖已有文件
new_filename = "new_file.txt"
try:
    with open(new_filename, 'x', encoding='utf-8') as f:
        f.write("This file is created with 'x' mode.\n")
    print(f"File '{new_filename}' created successfully.")
except FileExistsError:
    print(f"File '{new_filename}' already exists, not overwriting.")

# 7. 二进制文件读写
binary_filename = "binaryfile.bin"
data = b'\x00\x01\x02HelloBinary\x03\x04'
with open(binary_filename, 'wb') as bf:
    bf.write(data)

with open(binary_filename, 'rb') as bf:
    binary_content = bf.read()
    print("Binary file content:", binary_content)

# 8. 检查文件是否存在并删除文件
if os.path.exists(binary_filename):
    os.remove(binary_filename)
    print(f"Binary file '{binary_filename}' deleted.")

# 9. 获取文件大小
if os.path.exists(filename):
    file_size = os.path.getsize(filename)
    print(f"Size of '{filename}' is {file_size} bytes.")

# 10. 将文件内容复制到另一个文件
copy_filename = "copy_of_example.txt"
with open(filename, 'r', encoding='utf-8') as source, open(copy_filename, 'w', encoding='utf-8') as target:
    for line in source:
        target.write(line)
print(f"Copied content from '{filename}' to '{copy_filename}'.")

# 11. 使用 try/finally 手动关闭文件（不推荐，使用with语句更安全）
f = open(filename, 'r', encoding='utf-8')
try:
    print("First line of file using try/finally:", f.readline())
finally:
    f.close()

# 最终清理示例文件（可根据需要决定是否执行）
# os.remove(filename)
# os.remove(copy_filename)
# os.remove(new_filename)