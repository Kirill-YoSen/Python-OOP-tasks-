print("uzd 1:\n")
class Date: 
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    def get(self): 
        return f"{self.day}/{self.month}/{self.year}" 
    
class Human: 
    def __init__(self, name, surname, day, month, year, age, job):
        self.name = name
        self.surname = surname 
        self.birthday = Date(day, month, year)
        self.age = age
        self.job = job
    def family_member(self, member): 
        self.family = member
        member.family = self 
    def display_info(self): 
        print(f"[Person information]\nName: {self.name}\nSurname: {self.surname}\nBirthday: {self.birthday.get()}\nAge: {self.age}\nJob: {self.job}")
        try: 
            print(f"Family Member: {self.family.name}\n")
        except: 
            print(f"no family\n")
        
mom = Human("Jane", "Kreditka", 11, 9, 1980, 43, "teacher")
son = Human("Jhon", "Kreditka", 29, 12, 2004, 18, "student")
son.display_info()
son.family_member(mom)
son.display_info()
mom.display_info()
print("\nuzd.2\n")

        
# 2. uzdevums

# Izveido failu ar cilvēku sarakstu (.txt, .json. xlsx, .csv vai jebkurš cits formāts, ar kuru proti darboties):

# vārds, uzvārds;
# dzimšanas datums, mēnesis un gads;
# vecums;
# profesija;
# matu krāsa;
# acu krāsa;
# sarakstā esošie radinieki;
# radniecība.
# Nolasi izveidoto failu Python un izveido tik objektus, cik ir cilvēki - jāiekļauj visa failā esošā informācija.
import json
class Human1: 
    def __init__(self, name, surname, age, sex, day, month, year, job, hair, eyes):
        self.name = name 
        self.surname = surname
        self.age = age
        self.sex = sex  
        self.birthday = Date(day, month, year)
        self.job = job
        self.hair_color = hair 
        self.eye_color = eyes
        self.relations = [] 

    def family(self, member, relate, relateto): 
        self.relations.append([member.name, relate])
        member.relations.append([self.name, relateto])
    
    def displayInfo(self): 
        print(
            f"[PERSON DATA]\nName: {self.name}\nSurname: {self.surname}\nAge: {self.age}\nSex: {self.sex}\nBirthday: {self.birthday.get()}\nJob: {self.job}\nHair color: {self.hair_color}\nEye color: {self.eye_color}"
        )
        try: 
            s = ""
            for v in self.relations: 
                s = s + f"{v[1]} {v[0]}; "
            print(s)
        except: 
            pass

    def getAsJsonString(self): 
        json_str = '{"name":"'+self.name+'", "surname":"'+self.surname+'", "age":"'+str(self.age)+'", "sex": "'+self.sex+'", "birthday": "'+self.birthday.get()+'", "job": "'+self.job+'", "hair_color": "'+self.hair_color+'", "eye_color": "'+self.eye_color+'"'
        rel = ""
        try: 
            if len(self.relations) > 0: 
                rel = ', "relations": [' 
                for v in self.relations: 
                    rel = rel + f'"{v[1]} {v[0]}",'
                rel = rel[:-1]
                rel = rel + "]"
        except : 
            pass
        json_str = json_str + rel + "}"
        return json_str
        
mother = Human1("Sofia", "Light", 25, "female", 13, 5, 1998, "Teacher", "white", "blue")
father = Human1("Deniss", "Light", 27, "male", 12, 12, 1997, "software engineer","white", "grey")
mother.family(father, "husband", "wife")

son = Human1("Adam", "Light", 3, "male", 12, 12, 2020, "No", "blonde", "grey")
mother.family(son, "son", "mother")
father.family(son, "son", "father")

dict_arr = []
for v in [son, mother, father]: dict_arr.append(json.loads(v.getAsJsonString()))
with open('humans.json', 'w', encoding='utf-8') as f:
    json.dump(json.dumps(dict_arr), f, ensure_ascii=False, indent=4)
f.close()

data = ""
with open("humans.json", 'r', encoding="utf-8") as f: 
    data = json.load(f)
data = json.loads(data)
print(json.dumps(data, indent=4))

    
# 3. uzdevums
# Izvēlies jebkurus 2 no iepriekšējo gadu programmēšanas uzdevumiem un pārveido, izmantojot klases un objektus.
print("uzd 3:\n")


# 4. uzdevums

# Izveido klasi "Auto" ar atribūtiem "max_atrums" un "paterins";
# Izveido apakšklasi "Autobuss", kas manto visas klases "Auto" īpašības;
# Klasei "Auto" izveido metodi "sedvietas", kas ļauj noteikt, cik automašīnā ir sēdvietas;
# Papildini "Autobuss" apakšklasi ar metodi "sedvietas", kurā noklusējuma sēdvietu skaits ir 50;
# Klasei "Auto" pievieno atribūtu, kas nosaka auto krāsu, ar standarta vērtību "Balta";
# Klasei "Auto" pievieno metodi "cena", kas aprēķina cenu pēc formulas cena=sedvietas*100;
# Apakšklasei "Autobuss" pievieno metodi "cena", kas aprēķina cenu pēc formulas cena=sedvietas*10/100;
# Izveido vēlvienu apakšklasi pēc saviem ieskatiem un pievieno tai vismaz 2 metodes līdzīgi kā autobusa apakšklasei;
# Izveido 3 objektus - vienu ar galveno klasi, vienu ar apakšklasi "Autobuss" un vienu ar sevis izveidoto apakšklasi;
# Izmanto un parādi, ka visas izveidotās metodes darbojas korekti;
# Atrodi, ar kādu funkciju iespējams noteikt, vai objekts pieder kādai klasei un pārbaudi, vai izveidotie objekti pieder gan konkrētajai apakšklasei, gan galvenajai klasei "Auto".
class Auto: 
    def __init__(self, max_speed, fuel_usage):
        self.max_speed = max_speed
        self.fuel_usage = fuel_usage
    class Bus: 
        super().__init__("Auto")

# 5. uzdevums

# Izdomā, kur vēl varētu izmantot klases un apakšklases, izveido tās.
