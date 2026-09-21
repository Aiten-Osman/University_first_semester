
#zad1
def FindDayWinner(results):
    team1_wins = results.count("Team1")
    team2_wins = results.count("Team2")

    if team1_wins > team2_wins:
        return "Team1"
    elif team2_wins > team1_wins:
        return "Team2"
    else:
        return "Tie"
    
wins = input("Въведи отбор:")
list =(wins.split)
print(wins)


#zad2
def checkPerfectNum(numbers):
    sum = 0
    for i in range(1, numbers):
        if numbers % i == 0:
            sum += i
    if sum == numbers:
        return True
    else:
        return False
    
print(checkPerfectNum(int(input("Enter number: "))))





