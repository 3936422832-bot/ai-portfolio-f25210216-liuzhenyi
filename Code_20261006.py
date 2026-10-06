# vocab_tool.py 第三周作业成品
# 作业1：使用官方教程学到的 with 文件读写、列表推导式
# 作业2：功能② 生成填空题，把目标单词挖成____

def make_fill_blank(sentence: str, target_word: str) -> str:
    """生成挖空填空题：句子中的目标词替换成____"""
    blank_text = sentence.replace(target_word, "____")
    return blank_text


def main():
    # 原始例句库
    sentence_list = [
        "She enjoys reading novels in evening.",
        "He wants to finish his homework quickly.",
        "We should protect our natural environment."
    ]
    blank_word_list = ["novels", "homework", "environment"]

    # =========作业1 列表推导式（新语法）=========
    result_lines = [
        make_fill_blank(sent, word)
        for sent, word in zip(sentence_list, blank_word_list)
    ]

    # =========作业1 with语句安全写文件（官方教程文件读写）=========
    with open("练习.txt", "w", encoding="utf-8") as f:
        for line in result_lines:
            f.write(line + "\n")
    print("✅已经生成练习.txt")


if __name__ == "__main__":
    main()