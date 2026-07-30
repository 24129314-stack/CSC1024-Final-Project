# ==================
# reading platform.txt file
# ===================
def read_platforms():
    platforms_log = []
# ==================
# opening the file
# ===================
    try:
        with open('platforms.txt', 'r') as f:
          for line in f:
              line = line.strip()

# =======================================
# adding the number of details in the file
# =======================================
              if line != "":
                 details = line.split('|')
                 if len(details) >= 3:
                     platform_id = details[0]
                     platform_name = details[1]
                     followers = details[2]

                     platform = [
                          platform_id,
                          platform_name,
                          followers
                     ]
                     platform_log.append(platform)
# =================================
# incase platforms.txt is not found
# ================================
    except FileNotFoundError:
        print('platforms.txt not found')
       
    return platforms_log

# ====== testing ======
platforms_log = read_platforms()
print(platforms_log)

