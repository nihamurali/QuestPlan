
def get_planning(classes, total_time):


    # Define the classes with their durations and priorities
  
    total_priority = 0
    for c in classes:
        total_priority += c['priority']
    
    # Define the total available time slots
    total_time = total_time
    duration = total_time// total_priority

    for i in range(len(classes)):
        classes[i]['duration'] = classes[i]['priority'] * duration

    # Initialize the DP table
    dp = [[0 for _ in range(total_time + 1)] for _ in range(len(classes) + 1)]

    # Fill the DP table
    for i in range(1, len(classes) + 1):
        for w in range(1, total_time + 1):
            if classes[i-1]["duration"] <= w:#duration <= w: #
              #dp[i][w] = max(dp[i-1][w], dp[i-1][w-duration] + classes[i-1]["priority"])
                dp[i][w] = max(dp[i-1][w], dp[i-1][w-classes[i-1]["duration"]] + classes[i-1]["priority"])
            else:
                dp[i][w] = dp[i-1][w]

    # Backtrack to find the selected classes
    selected_classes = []
    w = total_time
    for i in range(len(classes), 0, -1):
        if dp[i][w] != dp[i-1][w]:
            #classes[i-1]['duration'] =duration
            selected_classes.append(classes[i-1])
            w -= classes[i-1]["duration"]
          #w -= duration

  # Print the selected classes
  # print("Selected classes for the timetable:")
  # for cls in selected_classes:
  #     #print(f"{cls['name']} (Duration: {cls['duration']}, Priority: {cls['priority']})")
  #     print(f"{cls['name']} (Duration: {duration}, Priority: {cls['priority']})")

    return selected_classes

# modules = [
#     {"name": "Math",  "priority": 1},
#     {"name": "Physics",  "priority": 2},
#     {"name": "Chemistry",  "priority": 3},
#     {"name": "Biology",  "priority": 4},
#   ]

# selected_modules = get_planning(modules)
# print(selected_modules)