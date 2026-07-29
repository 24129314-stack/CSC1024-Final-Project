# to do list
# engagement - record // display all // search specific engagement // update specific engagement // delete specific engagement // main option panel
# data to include : post id, likes, comments, shares, views


# this fuction is to record engagement of a post, user manually enters post ID, and other data
def record_engagement():
    post_id = input("Enter Post ID: ")
    try:
        likes = int(input("Enter Likes: "))
        comments = int(input("Enter Comments: "))
        shares = int(input("Enter Shares: "))
        views = int(input("Enter Views: "))
    except Exception as e:
        print(f"Invalid Reason: {e}")
        run_engagement_module()
    with open("engagement.txt", "a") as file:
        file.write(f"{post_id},{likes},{comments},{shares},{views}\n")
    print("Engagement recorded successfully!")

# this fuction is to display all engagement records by recenty added datas
# "for line in file" is used to read each line of the file, and print the data in a formatted way
# line.split(",") is used to split the data into a list, so that each data can be displayed separately in different rows
def display_engagement():
    with open("engagement.txt", "r") as file:
        print("\n===== Engagement Records =====")
        for line in file:
            data = line.split(",")
            print("Post ID :", data[0])
            print("Likes :", data[1])
            print("Comments :", data[2])
            print("Shares :", data[3])
            print("Views :", data[4])
            print("--------------------")

# this function is to allow user to search for the engagement data of a specific post by Post ID
def search_engagement():
    post_id = input("Enter Post ID: ")
    found = False
    with open("engagement.txt", "r") as file:
        for line in file:
            data = line.split(",")
            if data[0] == post_id:
                print("\n===== Engagement Found =====")
                print("Post ID :", data[0])
                print("Likes :", data[1])
                print("Comments :", data[2])
                print("Shares :", data[3])
                print("Views :", data[4])
                found = True
    if found == False:
        print("Post ID not found.")



# this function is to allow user to update engagement data of a specific post by Post ID
# [] is used to create a new list to store the updated data
# found is used to check if the post ID is found or not, if not found, it will print "Post ID not found."
# new_data.append() is used to add the updated data to the new list
# for line in new_data is used to write the updated data to the file
def update_engagement():
    post_id = input("Enter Post ID to update: ")
    found = False
    new_data = []
    with open("engagement.txt", "r") as file:
        for line in file:
            data = line.split(",")
            if data[0] == post_id:
                try:
                    likes = int(input("New Likes: "))
                    comments = int(input("New Comments: "))
                    shares = int(input("New Shares: "))
                    views = int(input("New Views: "))
                except Exception as e:
                    print(f"Invalid Reason: {e}")
                    run_engagement_module()

                new_data.append(f"{post_id},{likes},{comments},{shares},{views}\n")
                found = True
            else:
                new_data.append(line)
    with open("engagement.txt", "w") as file:
        for line in new_data:
            file.write(line)
    if found == False:
        print("Post ID not found.")
    else:
        print("Engagement updated successfully!")


# this fuction is to allow user to delete engagement data of a specific post by Post ID
def delete_engagement():
    post_id = input("Enter Post ID to delete: ")
    new_data = []
    with open("engagement.txt", "r") as file:
        for line in file:
            data = line.split(",")
            if data[0] != post_id:
                new_data.append(line)
    with open("engagement.txt", "w") as file:
        for line in new_data:
            file.write(line)
    print("Engagement deleted successfully!")

# while to true to ensure program runs until user selects exit option
def run_engagement_module():
    while True:
        print("\n===== Engagement Menu =====")
        print("1. Record Engagement")
        print("2. Display All Engagement")
        print("3. Search Engagement")
        print("4. Update Engagement")
        print("5. Delete Engagement")
        print("6. Exit")
        choice = input("Enter your choice: ")

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == "1":
            record_engagement()
        elif choice == "2":
            display_engagement()
        elif choice == "3":
            search_engagement()
        elif choice == "4":
            update_engagement()
        elif choice == "5":
            delete_engagement()
        elif choice == "6":
            print("Now exiting the engagament, see you soon!")
            break
        else:
            print("Invalid choice.")
