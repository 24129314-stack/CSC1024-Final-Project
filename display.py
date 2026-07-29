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
                  
                    date = details[0]
                    post_id = details[1]
                    platform = details[2]
                    status = details[3]
                    scheduled_time = details[4]
                

                    post = [
                        date,
                        post_id,
                        platform,
                        status,
                        scheduled_time
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
# ======================================================
# The layout of the content table 
# =====================================================
    print("\n--------- CONTENT CALENDAR ---------")

    print(f"{'date':<20}{'post_id':<20}{'platform':<20}{'status':<20}{'scheduled_time':<20}")
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
