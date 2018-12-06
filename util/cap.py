def capitalize(move):
    seperate = move.split("-")
    result = ""
    for move in seperate:
        result += move.capitalize() + " " 
    return result[:len(result)-1]
