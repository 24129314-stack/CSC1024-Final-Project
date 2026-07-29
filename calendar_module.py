from datetime import datetime


# ==============================
# defining the Function to read file posts
# ===============================
def read_posts():
    post_record = []

    try:
        with open("post.txt", "r") as file:
            for line in file:
                 line = line.strip()
                 if line != "":
                    details = line.split("|") 
                    if len(details) >= 5:
                        post_id = details[0]
                        platform = details[1]
                        caption = details[2]
                        scheduled_date = details[3]
                        status = details[4]
                

                    post = [
                         post_id,
                         platform,
                         caption,
                         scheduled_date,
                         status
                    ]

                    post_record.append(post)
# =============================================
# Incase posts.txt file is not found 
# =============================================
    except FileNotFoundError:
        print("post.txt not found.")

    return post_record

# ========================================================
# The final content calendar table will be displayed here :
# ========================================================
def display_content_calendar(post_record):

# ======================================================
# If the record or file is empty then display the record is not found
# ======================================================
   
    if not post_record:
        print("Not found.")
        return

    try:
        post_record.sort(
            key=lambda post: datetime.strptime(post[3], "%d/%m/%Y")
        )
    except ValueError:
        print("Unable to display calendar because an invalid date was found.")
        return
# ======================================================
# The layout of the content table 
# =====================================================
    print("\n--------- CONTENT CALENDAR ---------")


    print(
        f"{'Post ID':<10} | "
        f"{'Platform':<15} | "
        f"{'Caption':<35} | "
        f"{'Scheduled Date':<15} | "
        f"{'Status':<12}"
    )

    print("-" * 99)


    for post in post_record:
        print(
            f"{post[0]:<10} | "
            f"{post[1]:<15} | "
            f"{post[2]:<35} | "
            f"{post[3]:<15} | "
            f"{post[4]:<12}"
        )

# ================
# Main program
# ================
# if __name__ == "__main__":
def run_calendar_module():
    posts = read_posts()
    display_content_calendar(posts)
