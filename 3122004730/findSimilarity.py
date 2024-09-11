import sys
import difflib
import numpy as np
import os


def find_similarity(file1, file2):
    # 尝试打开file1
    with open(file1, 'r', encoding='utf-8') as f1:
        text1 = f1.read()
        if os.path.getsize(file1) == 0:
            return -1

    # 尝试打开file2
    with open(file2, 'r', encoding='utf-8') as f2:
        text2 = f2.read()
        # 检查file2是否为空
        if os.path.getsize(file2) == 0:
            return -1

    # 使用difflib比较两个文本
    matcher = difflib.SequenceMatcher(None, text1.split(), text2.split())
    similarity = np.around(matcher.ratio(), 2)

    return similarity
def clear_output_txt(output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        f.truncate(0)

def main():
    if len(sys.argv) != 4:
        print("Usage: python plagiarism_checker.py <original_file> <plagiarized_file> <output_file>")
        return

    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    try:
        similarity = find_similarity(original_file, plagiarized_file)  #计算相似度
        if similarity > 0:
            #返回值大于0表示查重顺利
            print(f"Similarity: {similarity}")
            # 将结果写入输出文件
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(f"{similarity:.2f}\n")
        else:
            #存在空文本
            print(f"Similarity: Empty file exists.")
    except FileNotFoundError:
        # 文件不存在
        print(f"ERROR:Can't find the file.Please check the file name.")
        clear_output_txt(output_file)
    except UnicodeDecodeError:
        # 文件乱码
        print(f"ERROR:Invalid UTF-8 encoded text exists.")
        clear_output_txt(output_file)
    except Exception as e:
        # 其他异常
        print(f"ERROR: {e.args[1]}.")
        clear_output_txt(output_file)


if __name__ == "__main__":
    main()

