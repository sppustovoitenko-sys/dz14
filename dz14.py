
# 1

class Event:

    def __init__(self, title, date):

        self.title = title

        self.date = date

    def show(self):

        print(f"Подія: {self.title}, Дата: {self.date}")

# 2

class Training(Event):

    def __init__(self, title, date, trainer):

        super().__init__(title, date)

        self.trainer = trainer

    def show(self):

        print(f"Тренування: {self.title}, Дата: {self.date}, Тренер: {self.trainer}")

class Birthday(Event):

    def __init__(self, title, date, person):

        super().__init__(title, date)

        self.person = person

    def show(self):

        print(f"День народження: {self.title}, Дата: {self.date}, Іменинник: {self.person}")

# 3

events = [

    Event("Зустріч", "01.06.2026"),

    Training("Python", "05.06.2026", "Олег"),

    Birthday("Свято", "10.06.2026", "Анна"),

    Event("Екзамен", "20.06.2026")

]

for event in events:

    event.show()

# 4

class Event:

    def __init__(self, title, date):

        self.title = title

        self.date = date

    def show(self):

        print(self.get_info())

    def get_info(self):

        return f"Подія: {self.title}, Дата: {self.date}"

class Training(Event):

    def __init__(self, title, date, trainer):

        super().__init__(title, date)

        self.trainer = trainer

    def get_info(self):

        return f"Тренування: {self.title}, Дата: {self.date}, Тренер: {self.trainer}"

class Birthday(Event):

    def __init__(self, title, date, person):

        super().__init__(title, date)

        self.person = person

    def get_info(self):

        return f"День народження: {self.title}, Дата: {self.date}, Іменинник: {self.person}"

event = Training("Python", "05.06.2026", "Олег")

print(event.get_info())

# 5

class OnlineEvent(Event):

    def __init__(self, title, date, link):

        super().__init__(title, date)

        self.link = link

    def show(self):

        print(f"Онлайн подія: {self.title}, Дата: {self.date}, Посилання: {self.link}")

# 6

online_event = OnlineEvent("Вебінар", "12.06.2026", "https://meet.com")

online_event.show()

# 7

events = [

    Event("Зустріч", "01.06.2026"),

    Training("Python", "05.06.2026", "Олег"),

    Birthday("Свято", "10.06.2026", "Анна"),

    OnlineEvent("Вебінар", "12.06.2026", "https://meet.com")

]

for event in events:

    print(event.get_info())
