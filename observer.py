from time import sleep
from group import Group
from member import Member
from jsonstream import Jsonstream


class Observer:

    # How many groups does info panel show
    # !! Warning !!
    # If you change this number, you must rewrite .kv file.
    show_num = 10


    def __init__(self):
        self.jsonstream = Jsonstream()
        self.group_list = []
        self.group_dict = self.jsonstream.get_group_dict()
        self.convert_dict2list()
        self.prev_group_dict = {}
        self.new_created_group = {}
        self.observing_groups = []


    def convert_dict2list(self):
        count = 0
        self.group_list = []
        for key in self.group_dict:
            g = self.group_dict[key]
            self.group_list.append(g)
            count += 1
        self.group_list.reverse()

    
    def get_observing_group_list(self):
        observing_group_list = []

        for i in range(self.show_num):
            dummy_member = Member(0,"",[],False,0,0,0,0)
            dummy_group = Group(0,[],[dummy_member],[],0,False,0,0,0,0,0,"","")
            observing_group_list.append(dummy_group)

        count = 0
        for g in self.group_list:
            if g.group_name in self.observing_groups:
                observing_group_list[count] = g
                count += 1
            if count >= self.show_num:
                break

        return observing_group_list


    def get_created_attention_group_dict(self):
        created_attention_group_dict = {}

        self.new_created_group = {}
        for key in self.group_dict:
            if key not in self.prev_group_dict:
                self.new_created_group[key] = self.group_dict[key]

        for key in self.new_created_group:
            g = self.new_created_group[key] 
            name = g.group_name
            if name in self.observing_groups:
                created_attention_group_dict[key] = g
        return created_attention_group_dict


    ## Just for debug
    def show_all_group(self):
        for key in self.group_dict:
            g = self.group_dict[key]
            name = g.group_name
            print("%d  :  %s" % (key, name))


    def renew(self):
        self.prev_group_dict = self.group_dict
        self.group_dict = self.jsonstream.get_group_dict()
        self.convert_dict2list()