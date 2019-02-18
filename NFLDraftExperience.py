import random
def main():
    print("Welcome to The NFL Draft Experince")
input("Press Enter to Start The Draft Process")

Name = input("Please Enter Your Name: ")
Position = input("Please Enter Your Position: ")
collegeTeam = input("Please Enter the Name of Your College: ")

possibleRound = ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Final', 'Undrafted']

draftRound = random.choice(possibleRound)

possibleTeam = ['Arizona Cardinals', 'Atlanta Falcons', 'Baltimore Ravens', 'Buffalo Bills', 'Carolina Panthers',
                'Chicago Bears', 'Cincinnati Bengals', 'Cleveland Browns', 'Dallas Cowboys', 'Denver Broncos',
                'Detroit Lions', 'Green Bay Packers', 'Houston Texans', 'Indianapolis Colts', 'Jacksonville Jaguars',
                'Kansas City Chiefs', 'Los Angeles Chargers', 'Los Angeles Rams', 'Miami Dolphins', 'Minnesota Vikings',
                'New England Patriots', 'New Orleans Saints', 'New York Giants', 'New York Jets', 'Oakland Raiders',
                'Philadelphia Eagles', 'Pittsburgh Steelers', 'San Francisco 49ers', 'Seattle Seahawks', 'Tampa Bay Buccaneers',
                'Tennessee Titans', 'Washington Redskins']   
                
draftTeam = random.choice(possibleTeam)
if draftRound != 'Undrafted':

    print("In the "+draftRound+" Round of the NFL Draft, The "+draftTeam+" have selected "+Name+"; "+Position+", "+collegeTeam)
else:
    print("Unfortanatly, you were not taken in this years NFL DRAFT, Lucky for you "+Name+ " The "+draftTeam+ " are willing to give you a chance to play "+Position+ " in the NFL!!!")

