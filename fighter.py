import random


class Fighters:
    """
    - a fighter is on a single team with many other players
    - a fighter plays in a match for a team
    """
    def __init__(self, name, skill):
        self.name = name

        # fighter skill rankings
        self.skill = skill

        # fighter salary
    def salary(self):
        return 5000 + self.skill*100


def generate_skill():
    # generate the skill level from stamina, strenght and intelligence
    # a fighter has atleast 5 on the stamina level
    stamina = random.randint(5, 34)

    def strength_generator(st):
        # if a fighter has a greater stamina than 20 his strenght is also greater than 20
        if st >= 20:
            strength = random.randint(20, 34)
            return strength
        elif st <= 20:
            strength = random.randint(5, 19)
            return strength

    def intelligence_generator(strength, st):
        # if a fighter has the average of strenght + stamina greater than 40 then his intelligence is bellow 15
        if (strength + st) // 2 >= 40:
            intelligence = random.randint(2, 14)
            return intelligence
        elif (strength + st) // 2 <= 40:
            intelligence = random.randint(15, 29)
            return intelligence

    return int(stamina + strength_generator(stamina) + intelligence_generator(strength_generator(stamina), stamina))

def generate_fighter():
    # generate a name form bellow
    names = [
        'AARON', 'ABDUL', 'AB', 'ABEL', 'ABRAHAM', 'ABRAM', 'ADALBER', 'ADAM', 'ADAN', 'ADOLFO', 'ADOLPH', 'ADRIAN',
        'AGUSTIN', 'AHMAD', 'AHMED', 'AL', 'ALAN', 'ALBERT', 'ALBERTO', 'ALDEN', 'ALDO', 'ALEC', 'ALEJAND', 'ALEX',
        'ALEXAND', 'ALEXIS', 'ALFONSO', 'ALFONZO', 'ALFRED', 'ALFREDO', 'ALI	0.0', 'ALLAN', 'ALLEN', 'ALONSO',
        'ALPHONS', 'ALPHONS', 'ALTON', 'ALVA', 'ALVARO', 'ALVIN', 'AMADO', 'AMBROSE', 'AMOS', 'ANDERSO', 'ANDRE',
        'ANDREA', 'ANDREAS', 'ANDRES', 'ANDREW', 'ANDY', 'ANGEL', 'ANGELO', 'ANIBAL', 'ANTHONY', 'ANTIONE', 'ANTOINE',
        'ANTON', 'ANTONE', 'ANTONIA', 'ANTONIO', 'ANTONY', 'ANTWAN', 'ARCHIE', 'ARDEN', 'ARIEL', 'ARLEN', 'ARLIE',
        'ARMAND', 'ARMANDO', 'ARNOLD', 'ARNOLDO', 'ARNULFO', 'ARON', 'ARRON', 'ART', 'ARTHUR', 'ARTURO', 'ASA'
        'BARTON', 'BASIL', 'BEAU', 'BEN	0.0', 'BENEDIC', 'BENITO', 'BENJAMI', 'BENNETT', 'BENNIE', 'BENNY', 'BENTON',
        'BERNARD', 'BERNARD', 'BERNIE', 'BERRY', 'BERT', 'BERTRAM', 'BILL', 'BILLIE', 'BILLY', 'BLAINE', 'BLAIR',
        'BLAKE', 'BO', 'BOB', 'BOBBIE', 'BOBBY', 'BOOKER', 'BORIS', 'BOYCE', 'BOYD', 'BRAD', 'BRADFOR', 'BRADLEY',
        'BRADLY', 'BRADY', 'BRAIN', 'BRANDEN', 'BRANDON', 'BRANT', 'BRENDAN', 'BRENDON', 'BRENT', 'BRENTON', 'BRET',
        'BRETT', 'BRIAN', 'BRICE', 'BRITT', 'BROCK', 'BRODERI', 'BROOKS', 'BRUCE', 'BRUNO', 'BRYAN', 'BRYANT', 'BRYCE',
        'BRYON', 'BUCK', 'BUD', 'BUDDY', 'BUFORD', 'BURL', 'BURT', 'BURTON', 'BUSTER', 'BYRON', 'CALEB', 'CALVIN',
        'CAMERON', 'CAREY', 'CARL', 'CARLO', 'CARLOS', 'CARLTON', 'CARMELO', 'CARMEN', 'CARMINE', 'CAROL', 'CARROL',
        'CARROLL', 'CARSON', 'CARTER', 'CARY', 'CASEY', 'CECIL', 'CEDRIC', 'CEDRICK', 'CESAR', 'CHAD', 'CHADWIC',
        'CHANCE', 'CHANG', 'CHARLES', 'CHARLEY', 'CHARLIE', 'CHAS', 'CHASE', 'CHAUNCE', 'CHESTER', 'CHET', 'CHI',
        'CHONG', 'CHRIS', 'CHRISTI', 'CHRISTO', 'CHRISTO', 'CHUCK', 'CHUNG', 'CLAIR', 'CLARENC', 'CLARK', 'CLAUD',
        'CLAUDE', 'CLAUDIO', 'CLAY', 'CLAYTON', 'CLEMENT', 'CLEMENT', 'CLEO', 'CLETUS', 'CLEVELA', 'CLIFF', 'CLIFFOR',
        'CLIFTON', 'CLINT', 'CLINTON', 'CLYDE', 'CODY', 'COLBY', 'COLE', 'COLEMAN', 'COLIN', 'COLLIN', 'COLTON',
        'COLUMBU', 'CONNIE', 'CONRAD', 'CORDELL', 'COREY', 'CORNELI', 'CORNELL', 'CORTEZ', 'CORY', 'COURTNE', 'COY',
        'CRAIG', 'CRISTOB', 'CRISTOP', 'CRUZ', 'CURT', 'CURTIS', 'CYRIL', 'CYRUS', 'DALE', 'DALLAS', 'DALTON', 'DAMIAN',
        'DAMIEN', 'DAMION', 'DAMON', 'DAN', 'DANA', 'DANE', 'DANIAL', 'DANIEL', 'DANILO', 'DANNIE', 'DANNY', 'DANTE',
        'DARELL', 'DAREN', 'DARIN', 'DARIO', 'DARIUS', 'DARNELL', 'DARON', 'DARREL', 'DARRELL', 'DARREN', 'DARRICK',
        'DARRIN', 'DARRON', 'DARRYL', 'DARWIN', 'DARYL', 'DAVE', 'DAVID', 'DAVIS', 'DEAN', 'DEANDRE', 'DEANGEL', 'DEE',
        'DEL', 'DELBERT', 'DELMAR', 'DELMER', 'DEMARCU', 'DEMETRI', 'DENIS', 'DENNIS', 'DENNY', 'DENVER', 'DEON',
        'DEREK', 'DERICK', 'DERRICK', 'DESHAWN', 'DESMOND', 'DEVIN', 'DEVON', 'DEWAYNE', 'DEWEY', 'DEWITT', 'DEXTER',
        'DICK', 'DIEGO', 'DILLON', 'DINO', 'DION', 'DIRK', 'DOMENIC', 'DOMINGO', 'DOMINIC', 'DOMINIC', 'DOMINIQ', 'DON',
        'DONALD', 'DONG', 'DONN', 'DONNELL', 'DONNIE', 'DONNY', 'DONOVAN', 'DONTE', 'DORIAN', 'DORSEY', 'DOUG',
        'DOUGLAS', 'DOUGLAS', 'DOYLE', 'DREW', 'DUANE', 'DUDLEY', 'DUNCAN', 'DUSTIN', 'DUSTY', 'DWAIN', 'DWAYNE',
        'DWIGHT', 'DYLAN', 'EARL', 'EARLE', 'EARNEST', 'ED	0.0', 'EDDIE', 'EDDY', 'EDGAR', 'EDGARDO', 'EDISON',
        'EDMUND', 'EDMUNDO', 'EDUARDO', 'EDWARD', 'EDWARDO', 'EDWIN', 'EFRAIN', 'EFREN', 'ELBERT', 'ELDEN', 'ELDON',
        'ELDRIDG', 'ELI	0.0', 'ELIAS', 'ELIJAH', 'ELISEO', 'ELISHA', 'ELLIOT', 'ELLIOTT', 'ELLIS', 'ELLSWOR', 'ELMER',
        'ELMO', 'ELOY', 'ELROY', 'ELTON', 'ELVIN', 'ELVIS', 'ELWOOD', 'EMANUEL', 'EMERSON', 'EMERY', 'EMIL', 'EMILE',
        'EMILIO', 'EMMANUE', 'EMMETT', 'EMMITT', 'EMORY', 'ENOCH', 'ENRIQUE', 'ERASMO', 'ERIC', 'ERICH', 'ERICK',
        'ERIK', 'ERIN', 'ERNEST', 'ERNESTO', 'ERNIE', 'ERROL', 'ERVIN', 'ERWIN', 'ESTEBAN', 'ETHAN', 'EUGENE',
        'EUSEBIO', 'EVAN', 'EVERETT', 'EVERETT', 'EZEKIEL', 'EZEQUIE'
    ]
    first_name = random.choice(names)
    last_name = random.choice(names)
    full_name = '{} {}'.format(first_name, last_name)
    skill = 5 + generate_skill()
    return Fighters(full_name, skill)
