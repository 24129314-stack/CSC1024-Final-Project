def read_platforms():
    platform_log = []

    try:
        with open('platforms.txt', 'r') as f:
          for line in f:
              line = line.strip()


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

    except FileNotFoundError:
        print('platforms.txt not found')
       
    return platform_log
