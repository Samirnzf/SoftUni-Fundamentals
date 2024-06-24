def register_user(database, username, license_plate):
    if username in database:
        return f"ERROR: already registered with plate number {database[username]}"
    else:
        database[username] = license_plate
        return f"{username} registered {license_plate} successfully"


def unregister_user(database, username):
    if username not in database:
        return f"ERROR: user {username} not found"
    else:
        del database[username]
        return f"{username} unregistered successfully"


def print_registered_users(database):
    for username, license_plate in database.items():
        print(f"{username} => {license_plate}")


def main():
    n = int(input())
    database = {}

    for _ in range(n):
        command = input().split()
        if command[0] == "register":
            username, license_plate = command[1], command[2]
            print(register_user(database, username, license_plate))
        elif command[0] == "unregister":
            username = command[1]
            print(unregister_user(database, username))

    print_registered_users(database)


if __name__ == "__main__":
    main()
