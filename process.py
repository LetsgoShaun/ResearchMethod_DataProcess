import os

# 遍历文件夹中所有的txt文件
for file_name in os.listdir():
    print(file_name)
    if file_name.endswith('.txt'):
        file_path = os.path.join(file_name)
        # 读取文件内容
        with open(file_path, 'r') as f:
            lines = f.readlines()
        # 删除前两行
        lines = lines[2:]
        # 将删除后的内容重新写入文件
        with open(file_path, 'w') as f:
            f.writelines(lines)

