import random # random digunakan agar damage yang diberikan acak 

# Class Robot yang mendefinisikan atribut dan metode robot
class Robot:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def get_name(self):
        return self.name

    def get_health(self):
        return self.health

    # Metode untuk menyerang robot lain
    def attack(self, other_robot):
        damage = random.randint(0, self.attack_power)
        print(f"{self.name} attacks {other_robot.get_name()} for {damage} damage!")
        other_robot.take_damage(damage)

    # Metode untuk menerima serangan
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # Metode untuk mengecek apakah robot sudah dikalahkan
    def is_defeated(self):
        return self.health == 0


# Class Battle yang mengelola pertarungan antara dua robot
class Battle:
    def __init__(self, robot1, robot2):
        self.robot1 = robot1
        self.robot2 = robot2

    # Method untuk memulai pertarungan
    def start_fight(self):
        print("Battle Start!")
        print("")
        while True:
            # Robot 1 menyerang robot 2
            self.robot1.attack(self.robot2)
            self.display_health()
            if self.robot2.is_defeated():
                print(f"{self.robot2.get_name()} is defeated!")
                print(f"-----  {self.robot1.get_name()} wins!  -----")
                break

            # Robot 2 menyerang robot 1
            self.robot2.attack(self.robot1)
            self.display_health()
            if self.robot1.is_defeated():
                print(f"{self.robot1.get_name()} is defeated!")
                print(f"-----  {self.robot2.get_name()} wins!  -----")
                break

    def display_health(self):
        print(f"=====   {self.robot1.get_name()} : {self.robot1.get_health()} health remains  =====")
        print(f"=====   {self.robot2.get_name()} : {self.robot2.get_health()} health remains  =====")
        print("")


# Class Game untuk mengelola daftar robot dan memulai permainan
class Game:
    def __init__(self):
        self.robots = []

    # Metode untuk menambahkan robot ke dalam daftar
    def add_robot(self, robot):
        self.robots.append(robot)

    # Method untuk memulai permainan
    def start_game(self):
        if len(self.robots) < 2: # menghitung jumlah robot dalam index self.robots
            print("You need at least two robots to start the battle.")
            return

        print("Choose robots for the battle:")
        for i, robot in enumerate(self.robots): # i mulai dari 0 sehingga ditambah 1 agar angka yang muncul mulai dari 1
            print(f"{i + 1}. {robot.get_name()}")
        print("===================")

        # Pemilihan robot pertama
        first_choice = int(input("Select the first robot: ")) - 1 # ada pengurangan 1 diakhir agar sesuai dengan i diatas (mulai dari 0)
        robot1 = self.robots[first_choice]

        # Pemilihan robot kedua
        second_choice = int(input("Select the second robot: ")) - 1
        robot2 = self.robots[second_choice]

        # Mulai pertarungan
        battle = Battle(robot1, robot2)
        battle.start_fight()


# Testing program
if __name__ == "__main__":
    # Membuat objek game
    game = Game()

    # Membuat beberapa robot dengan atribut yang berbeda-beda

    # spesifikasi attack_power disini tidak selalu konstan 
    # - karena ada fitur random yang digunakan (mulai dari 0 hingga nilai attack_power itu sendiri)
    robo1 = Robot("Atom", 100, 30)
    robo2 = Robot("Twin Cities", 110, 25)
    robo3 = Robot("Zeus", 120, 20)
    robo4 = Robot("Noisy Boy", 125, 15)
    # bisa ditambahkan jika diinginkan, kemudian add_robot dibawah

    # Menambahkan robot ke dalam game
    game.add_robot(robo1)
    game.add_robot(robo2)
    game.add_robot(robo3)
    game.add_robot(robo4)

    # Memulai permainan
    game.start_game()
