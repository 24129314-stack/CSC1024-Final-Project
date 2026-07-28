# ==============================
# defining the Function to read file posts
# ===============================
def read_post.txt():

    post_list = []

    try:
        with open("posts.txt", "r") as file:

            for line in file:

                line = line.strip()

                if line != "":

                    details = line.split("|")      
                  
                    atribute1 = details[0]
                    atribute2 = details[1]
                    atribute3 = details[2]
                    atribute4 = details[3]
                    atribute5 = details[4]
                

                    post = [
                        atribute1,
                        atribute2,
                        atribute3,
                        atribute4,
                        atribute5
                    ]

                    post_list.append(post)
# =============================================
# Incase posts.txt file is not found 
# =============================================
    except FileNotFoundError:
        print("posts.txt not found.")

    return post_list

# ========================================================
# The final content calendar table will be displayed here :
# ========================================================
def display_calendar(post_list):

# ======================================================
# If the record or file is empty then display the record is not found
# ======================================================
   
    if post_list [0]:
        print("Not found.")
        return
# ======================================================
# The layout of the content table 
# =====================================================
    print("\n--------- CONTENT CALENDAR ---------")

    print(f"{'Part1':<20}{'Part2':<20}{'Part3':<20}{'Part4':<20}{'Part5':<20}")

    print("-" * 70)

    for post in post_list:

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
