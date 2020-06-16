import urllib.request
import json
from group import Group
from member import Member


class Jsonstream:


    def get_json_object(self):
        url = "https://toonhq.org/api/v1/group/"
        headers = {"User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0"}
        request = urllib.request.Request(url=url, headers=headers)
        response = urllib.request.urlopen(request)
        json_object = json.loads(response.read().decode('utf8'))

        return json_object


    def get_members_list(self, member_list):
        members = []
        for toon in member_list:
            toon_id = toon["id"]
            toon_name = toon["toon_name"]
            irc_nick = toon["irc_nick"]
            owner = toon["owner"]
            num_players = toon["num_players"]
            joined = toon["joined"]
            species = toon["species"]
            color = toon["color"]
            m = Member(toon_id, toon_name, irc_nick, owner, num_players, joined, species, color)
            members.append(m)
        
        return members


    def get_group_dict(self):
        json_object = self.get_json_object()
        group_dict = {}

        for grp in json_object:
            group_id = grp["id"]
            options = grp["options"]
            member_list = grp["members"]
            members = self.get_members_list(member_list)
            expiration = grp["expiration"]
            num_messages = grp["num_messages"]
            special = grp["special"]
            created = grp["created"]
            updated = grp["updated"]
            last_keep_alive = grp["last_keep_alive"]
            keep_alives = grp["keep_alives"]
            group_type = grp["type"]
            district = grp["district"]
            location = grp["location"]
            g = Group(
                group_id, options, members, expiration, num_messages,
                special, created, updated, last_keep_alive, keep_alives,
                group_type, district, location
            )
            group_dict[group_id] = g

        return group_dict