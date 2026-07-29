# -------------------------------------
# GENERATE PERFORMANCE REPORT
# Shows total posts per platform, the best-performing post,
# and the most interactive platform.
# -------------------------------------
POSTS_FILE = "post.txt"
PLATFORMS_FILE = "platforms.txt"
ENGAGEMENT_FILE = "engagement.txt"

def generate_performance_report():
    # Generate the report content by reading the post and engagement files.
    report_content = build_performance_report()

    # Stop if the report could not be generated.
    if report_content is None:
        print("It is empty!")
        return

    # Display the completed report on the screen.
    print(report_content)


# -------------------------------------
# EXPORT REPORT TO FILE
# Saves the generated performance report into report.txt.
# -------------------------------------
def export_report():
    # Generate the same report content used for screen display.
    report_content = build_performance_report()

    # Stop if the report could not be generated.
    if report_content is None:
        print("It is empty!")
        return

    try:
        # Open report.txt in write mode.
        # Existing content will be replaced with the latest report.
        with open("report.txt", "w") as file:
            file.write(report_content)

        print("\nPerformance report exported successfully.")
        print("The report has been saved to report.txt.")

    except IOError:
        # Handle errors such as file permission problems.
        print("Error: Unable to export the report to report.txt.")


# -------------------------------------
# BUILD PERFORMANCE REPORT
# Reads data from post.txt and engagement.txt,
# calculates the required statistics, and returns
# the report as a formatted string.
# -------------------------------------
def build_performance_report():
    posts = []
    engagement_records = []

    # -------------------------------------
    # READ POST RECORDS
    # Expected format:
    # PostID|Platform|Caption|Date|Status
    # -------------------------------------
    try:
        with open(POSTS_FILE, "r") as file:
            for line in file:
                line = line.strip()

                # Ignore empty lines.
                if line == "":
                    continue

                data = line.split("|")

                # Only accept records with at least five fields.
                if len(data) >= 5:
                    post = {
                        "post_id": data[0].strip(),
                        "platform": data[1].strip(),
                        "caption": data[2].strip(),
                        "date": data[3].strip(),
                        "status": data[4].strip()
                    }

                    posts.append(post)
                else:
                    print(f"Warning: Invalid post record skipped: {line}")

    except FileNotFoundError:
        print(f"Error: {POSTS_FILE} was not found.")
        return None

    except IOError:
        print(f"Error: Unable to read {POSTS_FILE}.")
        return None

    # A performance report cannot be generated without post records.
    if not posts:
        print("No post records are available.")
        return None

    # -------------------------------------
    # READ ENGAGEMENT RECORDS
    # Supported formats:
    # PostID,Likes,Comments,Shares,Views
    # PostID|Likes|Comments|Shares|Views
    # -------------------------------------
    try:
        with open(ENGAGEMENT_FILE, "r") as file:
            for line in file:
                line = line.strip()

                # Ignore empty lines.
                if line == "":
                    continue

                # Support both comma-separated and pipe-separated records.
                if "|" in line:
                    data = line.split("|")
                else:
                    data = line.split(",")

                # Check that the record contains all five required fields.
                if len(data) < 5:
                    print(f"Warning: Invalid engagement record skipped: {line}")
                    continue

                try:
                    # Convert engagement values into integers for calculation.
                    likes = int(data[1].strip())
                    comments = int(data[2].strip())
                    shares = int(data[3].strip())
                    views = int(data[4].strip())

                    # Negative engagement values are not valid.
                    if likes < 0 or comments < 0 or shares < 0 or views < 0:
                        print(
                            f"Warning: Negative engagement record skipped: {line}"
                        )
                        continue

                    engagement = {
                        "post_id": data[0].strip(),
                        "likes": likes,
                        "comments": comments,
                        "shares": shares,
                        "views": views
                    }

                    engagement_records.append(engagement)

                except ValueError:
                    # Skip engagement records containing non-numeric values.
                    print(
                        f"Warning: Non-numeric engagement record skipped: {line}"
                    )

    except FileNotFoundError:
        # The report can still show post totals when no engagement file exists.
        print(
            f"Warning: {ENGAGEMENT_FILE} was not found. "
            "Engagement results will be unavailable."
        )

    except IOError:
        print(
            f"Warning: Unable to read {ENGAGEMENT_FILE}. "
            "Engagement results will be unavailable."
        )

    # -------------------------------------
    # COUNT TOTAL POSTS FOR EACH PLATFORM
    # -------------------------------------
    platform_post_counts = {}

    for post in posts:
        platform = post["platform"]

        if platform in platform_post_counts:
            platform_post_counts[platform] += 1
        else:
            platform_post_counts[platform] = 1

    # -------------------------------------
    # CREATE A POST LOOKUP TABLE
    # This makes it easier to find a post's platform by Post ID.
    # -------------------------------------
    post_lookup = {}

    for post in posts:
        post_lookup[post["post_id"]] = post

    # -------------------------------------
    # CALCULATE ENGAGEMENT RESULTS
    # Total engagement follows the project example:
    # likes + comments + shares + views
    # -------------------------------------
    best_post_id = None
    best_post_platform = None
    highest_engagement = -1

    platform_engagement = {}

    for engagement in engagement_records:
        post_id = engagement["post_id"]

        # Ignore engagement records whose Post ID does not exist.
        if post_id not in post_lookup:
            print(
                f"Warning: Engagement record for unknown Post ID "
                f"{post_id} was skipped."
            )
            continue

        total_engagement = (
            engagement["likes"]
            + engagement["comments"]
            + engagement["shares"]
            + engagement["views"]
        )

        platform = post_lookup[post_id]["platform"]

        # Add the engagement result to the platform total.
        if platform in platform_engagement:
            platform_engagement[platform] += total_engagement
        else:
            platform_engagement[platform] = total_engagement

        # Update the best-performing post when a higher total is found.
        if total_engagement > highest_engagement:
            highest_engagement = total_engagement
            best_post_id = post_id
            best_post_platform = platform

    # -------------------------------------
    # FIND THE MOST INTERACTIVE PLATFORM
    # -------------------------------------
    most_interactive_platform = None

    if platform_engagement:
        most_interactive_platform = max(
            platform_engagement,
            key=platform_engagement.get
        )

    # -------------------------------------
    # FORMAT THE REPORT
    # -------------------------------------
    report_lines = []

    report_lines.append("=" * 45)
    report_lines.append("PERFORMANCE REPORT")
    report_lines.append("=" * 45)

    report_lines.append("\nTotal Posts Per Platform")

    # Sort platform names alphabetically for consistent output.
    for platform in sorted(platform_post_counts):
        count = platform_post_counts[platform]

        # Use singular or plural wording appropriately.
        post_word = "post" if count == 1 else "posts"
        report_lines.append(f"{platform:<20}: {count} {post_word}")

    report_lines.append("\nBest Performing Post")

    if best_post_id is not None:
        report_lines.append(f"Post ID            : {best_post_id}")
        report_lines.append(f"Platform           : {best_post_platform}")
        report_lines.append(f"Total Engagement   : {highest_engagement}")
    else:
        report_lines.append("No valid engagement data available.")

    report_lines.append("\nMost Interactive Platform")

    if most_interactive_platform is not None:
        report_lines.append(
            f"{most_interactive_platform} "
            f"({platform_engagement[most_interactive_platform]} "
            f"total engagement)"
        )
    else:
        report_lines.append("No valid engagement data available.")

    report_lines.append("=" * 45)

    # Join all report lines into one complete string.
    return "\n".join(report_lines)