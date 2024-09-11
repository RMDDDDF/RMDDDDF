import sys
import difflib

def calculate_similarity(file1, file2):
    # 读取文件内容
    with open(file1, 'r', encoding='utf-8') as f1:
        text1 = f1.read()
    with open(file2, 'r', encoding='utf-8') as f2:
        text2 = f2.read()

    # 使用difflib比较两个文本
    matcher = difflib.SequenceMatcher(None, text1.split(), text2.split())
    similarity = matcher.ratio()

    return similarity

def main():
    if len(sys.argv) != 4:
        print("Usage: python plagiarism_checker.py <original_file> <plagiarized_file> <output_file>")
        return

    original_file = sys.argv[1]
    plagiarized_file = sys.argv[2]
    output_file = sys.argv[3]

    # 计算相似度
    similarity = calculate_similarity(original_file, plagiarized_file)

    # 将结果写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(f"{similarity:.2f}\n")

if __name__ == "__main__":
    main()