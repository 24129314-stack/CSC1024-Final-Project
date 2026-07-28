# =====================================
# SOCIAL MEDIA CONTENT PLANNER
# CSC1024 Programming Principles - Final Project
#
#Members:
#   - Saif Ferozkhan Pathan (Leader)
#   - Shao Pengyuan
#   - Chua Ming You
#   - Jaamunah Rahj
#   - Eugene Tee Yee Farn
#
#
# Task split:
#   - Menu System & Integration      -> [Saif Ferozkhan Pathan]
#   - Add New Post Idea              -> [Saif Ferozkhan Pathan]
#   - Update Post Status             -> [Shao Pengyuan]
#   - Delete Post                    -> [Shao Pengyuan]
#   - Record Engagement Metrics      -> [Chua Ming You]
#   - Display Content Calendar       -> [Jaamunah Rahj]
#   - Generate Performance Report    -> [Eugene Tee Yee Farn]
#   - Export Report to File          -> [Eugene Tee Yee Farn]
# =====================================


import os
from datetime import datetime
import spy_comment
POSTS_FILE = "posts.txt"
PLATFORMS_FILE = "platforms.txt"
ENGAGEMENT_FILE = "engagement.txt"


# -------------------------------------
# ADD NEW POST IDEA
# -------------------------------------
# Function for new post idea. It will take user input for Post ID, Platform, Caption, and Scheduled Date. The status will be set to Draft by default.
def add_new_post():
    """Lets the user add a new post. Status is set to Draft by default."""
    print("\n--- Add New Post ---")

    # User input for Post ID
    post_id = input("Enter Post ID: ").strip()
    if post_id == "":
        print("Post ID cannot be empty. Returning to menu.")
        return

    # Check the Post ID isn't used already
    if os.path.exists(POSTS_FILE):
        file = open(POSTS_FILE, "r")
        for line in file:
            existing_id = line.strip().split("|")[0]
            if existing_id == post_id:
                print("That Post ID already exists. Please use a unique ID.")
                file.close()
                return
        file.close()

    # User input for platform to post on
    platform = input("Enter Platform (e.g. Instagram, TikTok, X): ").strip()
    if platform == "":
        print("Platform cannot be empty. Returning to menu.")
        return

    #User input for post caption
    caption = input("Enter Caption: ").strip()
    if caption == "":
        print("Caption cannot be empty. Returning to menu.")
        return

    # User input for date to schedule the post
    date_input = input("Enter Scheduled Date (DD/MM/YYYY): ").strip()

    # Validate the date format
    try:
        datetime.strptime(date_input, "%d/%m/%Y")
    except ValueError:
        print("Invalid date format. Please use DD/MM/YYYY. Returning to menu.")
        return

    status = "Draft"

    #Save the new post to posts.txt text file
    try:
        file = open(POSTS_FILE, "a")
        file.write(f"{post_id}|{platform}|{caption}|{date_input}|{status}\n")
        file.close()
        print("Post added successfully.")
        print(f"Status: {status}")
    except IOError:
        print("Error: Could not save the post. Please try again.")


# -------------------------------------
# UPDATE POST STATUS -> [Teammate]
# Will change a post's status: Draft -> Scheduled -> Posted
# -------------------------------------
# def update_post_status():
#     print("\n[Update Post Status feature - to be added by teammate]")


# -------------------------------------
# RECORD ENGAGEMENT METRICS -> [Teammate]
# Will log likes, comments, shares, views for a Posted post into engagement.txt
# -------------------------------------
def record_engagement():
    print("\n[Record Engagement Metrics feature - to be added by teammate]")


# -------------------------------------
# DISPLAY CONTENT CALENDAR -> [Teammate]
# Will show all posts sorted by date with platform, caption preview, status
# -------------------------------------
def display_content_calendar():
    print("\n[Display Content Calendar feature - to be added by teammate]")


# -------------------------------------
# GENERATE PERFORMANCE REPORT -> [Teammate]
# Will show total posts per platform, best performing post, most interactive platform
# -------------------------------------
def generate_performance_report():
    print("\n[Generate Performance Report feature - to be added by teammate]")


# -------------------------------------
# EXPORT REPORT TO FILE -> [Teammate]
# Will save the performance report into report.txt
# -------------------------------------
def export_report():
    print("\n[Export Report feature - to be added by teammate]")


# -------------------------------------
# MENU SYSTEM
# -------------------------------------
def display_menu():
    print("\n=====================================")
    print("SOCIAL MEDIA CONTENT PLANNER")
    print("=====================================")
    print("1. Add New Post")
    print("2. Update Post Status")
    print("3. Record Engagement Metrics")
    print("4. Display Content Calendar")
    print("5. Generate Performance Report")
    print("6. Export Report to File")
    print("7. Exit")


# -------------------------------------
# INTEGRATION - ties every function together
# -------------------------------------
def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        try:
            choice = int(choice)
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 7.")
            continue

        if choice == 1:
            add_new_post()
        elif choice == 2:
            spy_comment.update_post_status()
        elif choice == 3:
            record_engagement()
        elif choice == 4:
            display_content_calendar()
        elif choice == 5:
            generate_performance_report()
        elif choice == 6:
            export_report()
        elif choice == 7:
            print("\nExiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 7.")


if __name__ == "__main__":
    main()