# test_database_operations.py

from users import add_user, update_user, delete_user
from teachers import add_teacher, update_teacher, delete_teacher
from subjects import add_subject, update_subject, delete_subject

def main():
    print("Тестирование операций с пользователями:")
    add_user("user1@example.com", 1)
    add_user("user2@example.com", 2)
    add_user("user3@example.com", 3)

    update_user("user1@example.com", "new_user1@example.com")
    delete_user("user2@example.com")

    print("\nТестирование операций с преподавателями:")
    add_teacher("teacher1@example.com", 101)
    add_teacher("teacher2@example.com", 102)
    add_teacher("teacher3@example.com", 103)

    update_teacher("teacher1@example.com", "new_teacher1@example.com")
    delete_teacher("teacher2@example.com")

    print("\nТестирование операций с предметами:")
    add_subject("Mathematics")
    add_subject("Science")
    add_subject("History")

    update_subject("Mathematics", "Advanced Mathematics")
    delete_subject("Science")

if __name__ == "__main__":
    main()
