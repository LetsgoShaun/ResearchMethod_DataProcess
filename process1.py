
import os

for file_name in os.listdir():
    if file_name.endswith(".txt"):
        file_path = os.path.join(file_name)
        with open(file_path, "r+") as file:
            lines = file.readlines()
            # 处理第一行
            first_line = lines[0].rstrip() + " county\n"
            lines[0] = first_line

            # 处理其他行
            for i in range(1, len(lines)):
                line = lines[i].rstrip()
                file_name_without_ext = file_name.split(".")[0]
                lines[i] = line + " " + file_name_without_ext + "\n"

            # 将修改后的内容写回文件
            file.seek(0)
            file.writelines(lines)
            file.truncate()