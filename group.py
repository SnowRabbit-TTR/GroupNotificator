import time
from member import Member


class Group:


    def __init__(self, group_id, options, members, expiration,
                 num_messages, special, created, updated, last_keep_alive,
                 keep_alives, group_type, district, location):
        self.group_id = group_id  # integer
        self.options = options  # list(integer)
        self.members = members  # list(member)
        self.expiration = expiration  # list
        self.num_messages = num_messages  # integer
        self.special = special  # boolean
        self.created = created  # integer (unix time)
        self.updated = updated  # integer (unix time)
        self.last_keep_alive = last_keep_alive  # integer (unix time)
        self.keep_alives = keep_alives  # integer
        self.group_type = group_type  # integer
        self.district = district  # string
        self.location = location  # string

        self.full_people = 0  # integer
        self.group_name = ""  # string
        self.image_name = ""  # string
        self.isfull = False
        self.set_group_name()
        self.last_activity = self.get_last_activity_time()  # string
        self.people = self.get_now_people()
        self.owner = self.get_owner_name()  # string
        self.image_name = "./image/" + self.image_name + ".jpg"


    ## Set group_name, full_people and image_name.
    def set_group_name(self):
        self.group_name = ""

        if self.group_type == 0:  # Dummy Group
            pass

        elif self.group_type == 1:  # Buillding
            kind = ""
            self.image_name = "building"
            for op in self.options:
                if op == 1:
                    additional = "One Story "
                elif op == 2:
                    additional = "Two Story "
                elif op == 3:
                    additional = "Three Story "
                elif op == 4:
                    additional = "Four Story "
                elif op == 5:
                    additional = "Five Story "
                elif op == 6:
                    additional = "Sellbot "
                    self.image_name = "building_sellbot"
                elif op == 7:
                    additional = "Cashbot "
                    self.image_name = "building_cashbot"
                elif op == 8:
                    additional = "Lawbot "
                    self.image_name = "building_lawbot"
                elif op == 9:
                    additional = "Bossbot "
                    self.image_name = "building_bossbot"
                kind += additional
            self.group_name += kind + "Building"
            self.full_people = 4

        elif self.group_type == 2:  # Sellbot Factory
            kind = ""
            for op in self.options:
                if op == 10:
                    additional = "Short "
                elif op == 11:
                    additional = "Long "
                elif op == 12:
                    additional = "Front "
                elif op == 13:
                    additional = "Side "
                elif op == 14:
                    additional = "Sound "
                elif op == 15:
                    additional = "Soundless "
                kind += additional
            self.group_name = kind + "Factory"
            self.full_people = 4
            self.image_name = "factory"

        elif self.group_type == 3:  # VP
            kind = ""
            for op in self.options:
                if op == 16:
                    additional = "No Shopping "
                elif op == 17:
                    additional = "SOS Shopping "
                kind += additional
            self.group_name = kind + "VP"
            self.full_people = 8
            self.image_name = "vp"

        elif self.group_type == 4:  # Mint
            kind = ""
            for op in self.options:
                if op == 18:
                    additional = "Coin "
                elif op == 19:
                    additional = "Dollar "
                elif op == 20:
                    additional = "Bullion "
                elif op == 21:
                    additional = "Sound "
                elif op == 22:
                    additional = "Soundless "
                kind += additional
            self.group_name = kind + "Mint"
            self.full_people = 4
            self.image_name = "mint"

        elif self.group_type == 5:  # CFO
            self.group_name = "CFO"
            self.full_people = 8
            self.image_name = "cfo"

        elif self.group_type == 6:  # DA Office
            self.group_name = "DA Office"
            for op in self.options:
                if op == 23:
                    additional = " A"
                elif op == 24:
                    additional = " B"
                elif op == 25:
                    additional = " C"
                elif op == 26:
                    additional = " D"
                self.group_name += additional
            self.full_people = 4
            self.image_name = "da"

        elif self.group_type == 7:  # CJ
            self.group_name = "CJ"
            self.full_people = 8
            self.image_name = "cj"

        elif self.group_type == 8:  # Golf Course
            kind = ""           
            for op in self.options:
                if op == 27:
                    additional = "Front 3 "
                elif op == 28:
                    additional = "Middle 6 "
                elif op == 29:
                    additional = "Back 9 "
                kind += additional
            self.group_name = kind + "Golf Course"
            self.full_people = 4
            self.image_name = "golfcourse"

        elif self.group_type == 9:  # CEO
            self.group_name = "CEO"
            self.full_people = 8
            self.image_name = "ceo"

        elif self.group_type == 10:  # Toontask
            self.group_name = "Toontask"
            self.full_people = 8
            self.image_name = "toontask"

        elif self.group_type == 11:  # Gag Training
            kind = ""           
            for op in self.options:
                if op == 30:
                    additional = "Toon-Up "
                elif op == 31:
                    additional = "Trap "
                elif op == 32:
                    additional = "Lure "
                elif op == 33:
                    additional = "Sound "
                elif op == 34:
                    additional = "Throw "
                elif op == 35:
                    additional = "Squirt "
                elif op == 36:
                    additional = "Drop "
                kind += additional
            self.group_name = kind + "Gag Training"
            self.full_people = 7
            self.image_name = "training"

        elif self.group_type == 13:  # Kart Racing
            kind = ""           
            for op in self.options:
                if op == 44:
                    additional = "Competitive "
                elif op == 45:
                    additional = "For Win Trading "
                kind += additional
            self.group_name = kind + "Kart Racing"
            self.full_people = 4
            self.image_name = "training"

        # TODO: Other gropup is need to be added.
        else:  # others
            self.group_name = "unknown"
            self.full_people = "?"


    ## Return how many people in the group. (ex: 4 / 8)
    def get_now_people(self):

        if self.group_type == 0:
            return ""

        people = 0
        member_list = self.members
        for toon in member_list:
            people += toon.num_players
        
        people_status = str(people) + " / " + str(self.full_people)
        if people == self.full_people:
            self.isfull = True

        return people_status


    ## Return the name of toon who established the group.
    def get_owner_name(self):
        member_list = self.members
        for toon in member_list:
            if toon.owner == True:
                return toon.toon_name
        return ""


    ## Return the time from last activity.
    def get_last_activity_time(self):
        
        if self.group_type == 0:
            return ""

        status = ""
        nowtime = int(time.time())
        last_activity = nowtime - self.updated
        if last_activity < 10:
            status = "a few seconds ago"
        elif last_activity < 60:
            status = "%d seconds ago" % last_activity
        elif last_activity < 120:
            status = "a minute ago"
        else:
            minutes = (int)((last_activity)/60)
            status = "%d minutes ago" % minutes
        return status