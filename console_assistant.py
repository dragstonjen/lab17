
from assistant import Assistant

def main():
    assistant = Assistant()
    print("Віртуальний помічник. Введіть /help для перегляду команд.")

    while True:
        command = input("Введіть команду: ").strip()

        if command == "/add":
            note = input("Введіть нотатку: ")
            assistant.add_note(note)
            print("Нотатку додано.")

        elif command == "/list":
            notes = assistant.list_notes()
            print("\n".join(notes) if notes else "Немає нотаток.")

        elif command == "/search":
            keyword = input("Введіть ключове слово: ")
            results = assistant.search_notes(keyword)
            print("\n".join(results) if results else "Нічого не знайдено.")

        elif command == "/help":
            print("/add /list /search /exit")

        elif command == "/exit":
            print("Вихід...")
            break

        else:
            print("Невідома команда. Введіть /help.")

if __name__ == "__main__":
    main()
