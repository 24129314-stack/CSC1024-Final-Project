from datetime import datetime


# ==============================
# defining the Function to read file posts
# ===============================
def read_posts():
    post_record = []

    try:
        with open("posts.txt", "r") as file:
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
        print("posts.txt not found.")

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

    post_record.sort(
        key=lambda post: datetime.strptime(post[3], "%d/%m/%Y")
            )
# ======================================================
# The layout of the content table 
# =====================================================
    print("\n--------- CONTENT CALENDAR ---------")

    print(f"{'Post_id':<20}{'Platform':<20}{'Caption':<20}{'Scheduled_date':<20}{'Status':<20}")
    print("-" * 100)

    for post in post_record:

        print(
            f"{post[0]:<20}"
            f"{post[1]:<20}"
            f"{post[2]:<20}"
            f"{post[3]:<20}"
            f"{post[4]:<20}"
        )

# ================
# Main program
# ================
posts = read_posts()
display_content_calendar(posts)
