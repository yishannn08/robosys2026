import random

WORDS = [
    {"word": "apple", "hint": "りんご"},
    {"word": "banana", "hint": "バナナ"},
    {"word": "cat", "hint": "ネコ"},
    {"word": "dog", "hint": "イヌ"},
    {"word": "sakura", "hint": "さくら"},
]


def shuffle_word(word):
    letters = list(word)
    random.shuffle(letters)

    shuffled = "".join(letters)
    if shuffled == word and len(word) > 1:
        return shuffle_word(word)

    return shuffled


def start_game():
    score = 0
    lives = 3
    mistakes = []
    questions = random.sample(WORDS, len(WORDS))

    print("\n=== WORD QUEST ===")
    print("日本語の意味を見て、並び替えられた英単語を入力してください。")
    print("答えるには英単語を入力してください。\n")

    for item in questions:
        if lives <= 0:
            break

        answer = item["word"]
        scrambled = shuffle_word(answer)

        print(f"ヒント（日本語）：{item['hint']}")
        print(f"並び替え：{scrambled}")
        print(f"スコア：{score}　ライフ：{lives}")

        user_answer = input("答え：").strip().lower()

        if user_answer == answer:
            score += 10
            print("正解！ +10点\n")
        else:
            lives -= 1
            mistakes.append(item)
            print(f"不正解。正しい答えは「{answer}」です。\n")

    print("=== 終了 ===")
    print(f"スコア：{score}")
    print(f"残りライフ：{lives}")

    if mistakes:
        print("\n復習リスト：")
        for item in mistakes:
            print(f"- {item['word']}：{item['hint']}")

    print()


def main():
    while True:
        print("WORD QUEST")
        print("1. Casual Mode")
        print("2. 終了")

        choice = input("選択：").strip()

        if choice == "1":
            start_game()
        elif choice == "2":
            print("ゲームを終了します。")
            break
        else:
            print("1または2を入力してください。\n")


if __name__ == "__main__":
    main()
