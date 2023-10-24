with open("input") as file:
    lines = file.readlines()
    """
    Solution #1

    Doesn't scale well for pt.2
    """
    # for line in lines:
    #         for i in range(len(line)):
    #             if i + 3 == len(line):
    #                 break
    #             if line[i] not in [line[i+1], line[i+2], line[i+3]] \
    #             and line[i+1] not in [line[i+2], line[i+3]] \
    #             and line[i+2] != line[i+3]:
    #                 print(i+4) # Print answer
    #                 print(line[i],line[i+1],line[i+2],line[i+3], sep="") 
    #                 break

    """
    Solution #2
    
    Using sets
    """
    for line in lines:
        for i in range(len(line)):
            if len(set(line[i:i+14])) == len(line[i:i+14]):
                print(i+14)
                break