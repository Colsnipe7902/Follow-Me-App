class FollowMeApp:
    def __init__(self):
        self.friends = []

    def view_friends(self):
        print("Friends you're following:")
        for friend in self.friends:
            print(f"- {friend}")
        print()

    def follow_friend(self):
        new_friend = input("Enter the name of the friend you want to follow: ")
        if new_friend not in self.friends:
            self.friends.append(new_friend)
            print(f"You are now following {new_friend}")
        else:
            print(f"You are already following {new_friend}")

    def unfollow_friend(self):
        friend_to_unfollow = input("Enter the name of the friend you want to unfollow: ")
        if friend_to_unfollow in self.friends:
            self.friends.remove(friend_to_unfollow)
            print(f"You have unfollowed {friend_to_unfollow}")
        else:
            print(f"You are not following {friend_to_unfollow}")

    def run_app(self):
        while True:
            print("\nOptions:")
            print("1. View friends")
            print("2. Follow new friend")
            print("3. Unfollow friend")
            print("4. Quit")

            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                self.view_friends()
            elif choice == "2":
                self.follow_friend()
            elif choice == "3":
                self.unfollow_friend()
            elif choice == "4":
                print("Exiting FollowMe app. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    follow_me_app = FollowMeApp()
    follow_me_app.run_app()
