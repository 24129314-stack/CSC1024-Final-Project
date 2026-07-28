# Function to update the status of a social media post based on its current state.
# Status flow: Draft -> Scheduled -> Posted (terminal state).
def update_post_status():
    # Open the posts file in read mode and load all lines into a list.
    with open('post.txt', 'r') as f:
        posts = f.readlines()

    # Prompt the user to enter the ID of the post they want to update.
    post_id = input('Please input post id: ')

    # Iterate through each post to find the one matching the given ID.
    for i in range(len(posts)):
        # Parse the post record: fields are separated by the '|' delimiter.
        data = posts[i].strip().split("|")
        # The status is stored in the 5th field (index 4).
        status = data[4]

        # Check if the current post's ID matches the user-provided ID.
        if post_id == data[0]:
            # Transition the status: Draft becomes Scheduled.
            if status == 'Draft':
                data[4] = 'Scheduled'
            # Transition the status: Scheduled becomes Posted.
            elif status == 'Scheduled':
                data[4] = 'Posted'
            # Posted is a terminal state — no further transitions allowed.
            elif status == 'Posted':
                print("This post has already been posted.")
                return

            # Reconstruct the post line with the updated status and write it back to the list.
            posts[i] = "|".join(data) + "\n"
            # Exit the loop once the matching post has been found and updated.
            break

    # This else clause belongs to the for loop — it executes only if the loop
    # completed without hitting a 'break', meaning the post ID was not found.
    else:
        print("Post with ID not found.")
        return

    # Write the updated list of posts back to the file, overwriting the old content.
    with open('post.txt', 'w') as f:
        f.writelines(posts)

    # Notify the user that the update was successful.
    print("Status updated successfully!")









