from game.lifeclat import *
card_name = decodefich("card/name.txt")
card_att = decodefich("card/att.txt")
card_def = decodefich("card/def.txt")
card_nb = decodefich("card/nb.txt")
card_cout = decodefich("card/cout.txt")
card_effect = decodefich("card/effect.txt")
card_name = card_name.split('/')
card_att = card_att.split('/')
card_def = card_def.split('/')
card_nb = card_nb.split('/')
card_cout = card_cout.split('/')
card_effect = card_effect.split("/")
class Card:
    def __init__(self):
        self.card_used = ""
        self.card_att = ""
        self.card_def = ""
        self.card_name = ""
        self.card_effect = ""
        self.card_cout = ""
        self.card_tout = len(card_nb)-1
    def var_for_card(self, nb):
        self.card_used = card_nb[nb]
        self.card_name = card_name[nb]
        self.card_att = card_att[nb]
        self.card_cout = card_cout[nb]
        self.card_def = card_def[nb]
        self.card_effect = card_effect[nb]
    def set_newcard_by_nb(self, nbe):
        Card.var_for_card(self, card_nb.index(str(nbe)))
    def set_newcard_by_name(self, name):
        Card.var_for_card(self, card_name.index(str(name)))
    def cout_carte_nb(self, nb):
        return card_cout(card_nb.index(str(nb)))
    def cout_carte_name(self, name):
        return card_cout(card_name.index(str(name)))
    def nb_by_name(self, name):
        return card_nb[card_name.index(str(name))]
    def name_by_nb(self, nb):
        return card_name[card_nb.index(str(nb))]
class board_card:
    def __init__(self, user):
        self.names = []
        self.defs = []
        self.atts = []
        self.user = user
        self.card = Card()
        self.effect = ""
    def new_card(self, name):
        self.card.set_newcard_by_name(name)
        self.names.append(name)
        self.defs.append(self.card.card_def)
        self.atts.append(self.card.card_att)
        self.effect = self.card.card_effect
        if self.user == "user":
            if self.effect != "":
                exec(self.effect)
            card_planu.insert(END, name)
            user_main.delete(user_main.get(0, END).index(name))
        else:
            if self.effect != "":
                exec(self.effect)
            card_plane.insert(END, name)
        self.att_carte(name, 0)
    def delete_carte(self, name):
        carte_data = self.names.index(name)
        del self.atts[carte_data]
        del self.defs[carte_data]
        del self.names[carte_data]
        if self.user == "user":
            card_planu.delete(card_planu.get(0, END).index(name))
        else:
            card_plane.delete(card_plane.get(0, END).index(name))
        photo = ImageTk.PhotoImage(Image.open('card/png/0.png'))
        Card_view.configure(image=photo)
    def att_carte(self, name, degats):
        self.defs[self.names.index(name)] = str(int(self.defs[self.names.index(name)])-int(degats))
        if int(self.defs[self.names.index(name)]) <= 0:
            self.delete_carte(name)
    def ulife(self, x):
        if self.user == "user":
            change_life("u", -int(x))
        else:
            change_life("e", -int(x))
    def elife(self, x):
        if self.user == "user":
            change_life("e", int(x))
        else:
            change_life("u", int(x))
    def uclat(self, x):
        if self.user == "user":
            change_eclat("u", int(x))
        else:
            change_eclat("e", int(x))
    def mylife(self):
        if self.user == "user":
            return userlife.get()
        else:
            return ennemilife.get()