# Strong Password Checker
# written by Georgia Berar as a technical test for UMT Software

# password checker class
# validates a strong password and constructs the strongest password with minimal changes
class PasswordChecker:

    def __init__(self, password):
        self.password = password
        self.__lowercase = None  # positions of lowercase characters
        self.__uppercase = None  # positions of uppercase characters
        self.__digits = None  # positions of digit characters
        self.__repeated = None  # repeated character positions to be replaced
        self.__symbols = None  # positions of symbols
        self.count = 0  # keeps count of changes made

        self.__conditions()  # initialises the condition checking variables

    # verifies the password and constructs the associated variables
    def __conditions(self):
        self.__lowercase = []
        self.__uppercase = []
        self.__digits = []
        self.__repeated = []
        self.__symbols = []

        repeating = 1  # keeps count of adjacent repeating characters
        for pos in range(len(self.password)):
            if pos > 0:
                if self.password[pos] == self.password[pos - 1]:
                    repeating += 1
                if self.password[pos] != self.password[pos - 1]:
                    for i in range(pos - repeating + 2, pos, 3):
                        self.__repeated.append(i)
                    repeating = 1
                elif pos == len(self.password) - 1:
                    for i in range(pos - repeating + 3, pos + 1, 3):
                        self.__repeated.append(i)
                    repeating = 1
            if self.password[pos].islower():
                self.__lowercase.append(pos)
            elif self.password[pos].isupper():
                self.__uppercase.append(pos)
            elif self.password[pos].isdigit():
                self.__digits.append(pos)
            else:
                self.__symbols.append(pos)

    # receives a character and a position
    # checks if new character conflicts with neighbours
    # returns recommended value for replacement
    def __recommended(self, char, pos):
        recommended = char
        next_char, prev_char = None, None
        if pos + 1 < len(self.password):
            next_char = self.password[pos + 1]
        if pos - 1 > 0:
            prev_char = self.password[pos - 1]

        if char.islower():
            while recommended == next_char or recommended == prev_char:
                new = chr(ord(char) + 1)
                if recommended == 'z':
                    new = 'a'
                recommended = new
        if char.isupper():
            while recommended == next_char or recommended == prev_char:
                new = chr(ord(char) + 1)
                if recommended == 'Z':
                    new = 'A'
                recommended = new
        if char.isdigit():
            while recommended == next_char or recommended == prev_char:
                new = str(int(next_char) + 1)
                if recommended == '9':
                    new = '0'
                recommended = new

        return recommended

    # receives a character and a position
    # updates password and variables according to one change (insertion/replacement of given char on pos)
    def __update(self, char, pos):
        new = self.__recommended(char, pos)

        if char.islower():
            self.__lowercase.append(pos)
        elif char.isupper():
            self.__uppercase.append(pos)
        elif char.isdigit():
            self.__digits.append(pos)
        else:
            self.__symbols.append(pos)

        if pos == len(self.password):
            self.password += new

        else:
            old = self.password[pos]
            if pos in self.__repeated:
                self.__repeated.remove(pos)
            if old.islower():
                self.__lowercase.remove(pos)
            elif old.isupper():
                self.__uppercase.remove(pos)
            elif old.isdigit():
                self.__digits.remove(pos)
            else:
                self.__symbols.remove(pos)
            self.password = self.password[:pos] + new + self.password[pos + 1:]

        self.count += 1

    # finds appropriate position and replaces with given character
    def __replace(self, char):
        pos = None

        # if length is insufficient, insert new character
        if len(self.password) < 6:
            pos = len(self.password)

        # if there are repeating characters, replace one of them
        elif len(self.__repeated) > 0:
            pos = self.__repeated[-1]

        # if there is any symbol position, replace it
        elif len(self.__symbols) > 0:
            pos = self.__symbols[-1]

        # if there are available uppercase/lowercase/digit positions, replace
        else:
            if char.islower():
                if len(self.__uppercase) > 1:
                    pos = self.__uppercase[-1]

                elif len(self.__digits) > 1:
                    pos = self.__digits[-1]
            if char.isupper():
                if len(self.__lowercase) > 1:
                    pos = self.__lowercase[-1]

                elif len(self.__digits) > 1:
                    pos = self.__digits[-1]
            if char.isdigit():
                if len(self.__uppercase) > 1:
                    pos = self.__uppercase[-1]

                elif len(self.__lowercase) > 1:
                    pos = self.__lowercase[-1]

        # insert new character
        if pos is None:
            pos = len(self.password)

        self.__update(char, pos)

    # eliminates unnecessary characters
    def __remove(self):

        # attempts to remove problematic repeating characters
        while len(self.__repeated) > 0:
            pos = self.__repeated[0]
            self.password = self.password[:pos] + self.password[pos + 1:]
            self.__conditions()
            self.count += 1
            if len(self.password) <= 20:
                return

        # removes characters if it doesn't break conditions
        i = 0
        while i < len(self.password):
            if 0 < i < len(self.password):
                if self.password[i - 1] != self.password[i + 1]:
                    if self.password[i].islower():
                        if len(self.__lowercase) > 1:
                            self.password = self.password[:i] + self.password[i + 1:]
                            self.__conditions()
                            self.count += 1
                    elif self.password[i].isupper():
                        if len(self.__uppercase) > 1:
                            self.password = self.password[:i] + self.password[i + 1:]
                            self.__conditions()
                            self.count += 1
                    elif self.password[i].isdigit():
                        if len(self.__digits) > 1:
                            self.password = self.password[:i] + self.password[i + 1:]
                            self.__conditions()
                            self.count += 1
                    else:
                        self.password = self.password[:i] + self.password[i + 1:]
                        self.__conditions()
                        self.count += 1
            else:
                if self.password[i].islower():
                    if len(self.__lowercase) > 1:
                        self.password = self.password[:i] + self.password[i + 1:]
                        self.__conditions()
                        self.count += 1
                elif self.password[i].isupper():
                    if len(self.__uppercase) > 1:
                        self.password = self.password[:i] + self.password[i + 1:]
                        self.__conditions()
                        self.count += 1
                elif self.password[i].isdigit():
                    if len(self.__digits) > 1:
                        self.password = self.password[:i] + self.password[i + 1:]
                        self.__conditions()
                        self.count += 1
                else:
                    self.password = self.password[:i] + self.password[i + 1:]
                    self.__conditions()
                    self.count += 1
            if len(self.password) <= 20:
                return
            i += 1

    # performs least amount of changes to construct a strong password
    # returns new password or 0 if password is already strong
    def improve(self):
        if ' ' in self.password:
            raise Exception('Invalid password: no spaces allowed')

        # if there are too many characters
        if len(self.password) > 20:
            self.__remove()

        # if there are no lowercase letters
        if len(self.__lowercase) == 0:
            self.__replace('a')

        # if there are no uppercase letters
        if len(self.__uppercase) == 0:
            self.__replace('A')

        # if there are no digits
        if len(self.__digits) == 0:
            self.__replace('0')

        # if there are repeating characters
        while len(self.__repeated) > 0:
            self.__update('a', self.__repeated[-1])

        # if there are too few characters
        while len(self.password) < 6:
            self.__update('A', len(self.password))

        if self.count == 0:
            return 0
        else:
            return self.password


# application entry point
# main loop where user can input a password to check
def main():
    print('\nInsert password or press enter to generate:')
    print('[Press . to exit]')
    while True:
        try:
            password = input('\n')
            if password == ".":
                return
            else:
                password_checker = PasswordChecker(password)
                password = password_checker.improve()
                if password == 0:
                    print(password)
                else:
                    print('Improved password: ' + password)
                    print('Number of changes made: ' + str(password_checker.count))
        except Exception as ex:
            print(ex)


if __name__ == '__main__':
    main()
