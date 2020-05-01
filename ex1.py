# Troy Prebenda
# TP7, Ex1: Messagerie/SMS class

#!/usr/bin/python
from datetime import datetime
import re


class SMS:
    # numero et texte sont une chaine de caracteres; dateheure- de type datetime
    def __init__(self, numero, texte, dateheure=None):
        self.numero = numero
        self.texte = texte
        if not dateheure:
            self.heure = datetime.now()
        else:
            self.heure = dateheure

        self.vu = False

    def __str__(self):
        if self.vu == True:
            return self.texte
        else:
            return '+' + self.texte
        
    def __contains__(self, mot):
        s = self.texte.split(" ")
        for curr_mot in s:
            cleaned_mot = re.sub(r'\W+', '', curr_mot)
            if curr_mot == mot or cleaned_mot == mot:
                return True

        return False

    def estvu(self):
        self.vu = True
    
    def nonvu(self):
        self.vu = False


class Messagerie:
    def __init__(self):
        self.all_m = []
    
    def __getitem__(self, i):
        if (self.all_m and i < len(self.all_m)):
            return self.all_m[i]
        else:
            raise IndexError('Invalid index')
            

    def __delitem__(self, i):
        if (self.all_m and i < len(self.all_m)):
            del self.all_m[i]
        else:
            raise IndexError('Message does not exist for removal')
    

    def __iter__(self):
        self.count = 0
        return self
    
    def __next__(self):
        try:
            mes = self.all_m[self.count]
        except IndexError:
            raise StopIteration

        self.count += 1
        return mes


    def ajoute(self, m):
        self.all_m.append(m)

    def __len__(self):
        return len(self.all_m)

    def __str__(self):
        s = ""
        for m_idx in range(len(self.all_m)):
            s += str(self.all_m[m_idx])
            if m_idx != len(self.all_m) - 1:
                s += '\n'
        return s


    def nonLu(self):
        m_len = len(self.all_m)
        return [idx for idx in range(m_len) if self.all_m[idx].vu == False]

    def messagesNonLus(self):
        for mes in self.all_m:
            if not mes.vu:
                print(mes)
                mes.estvu()
    
    def recherchenum(self, num):
        m_len = len(self.all_m)
        return [idx for idx in range(m_len) if self.all_m[idx].numero == num]

    def effacenum(self, num):
        num_deleted = 0
        new_message_list = self.all_m[:]

        for mes in self.all_m:
            if mes.numero == num:
                new_message_list.remove(mes)
                num_deleted += 1

        self.all_m = new_message_list
        return num_deleted

    

if __name__== "__main__":
    m = Messagerie()
    s1 = SMS("555", "Salut")
    s2 = SMS("555", "Bonjour")
    s3 = SMS("444", "Hello, ca va?")
    s4 = SMS("123", "Bonjour bonjour!")
    s5 = SMS("444", "Allo")
    m.ajoute(s1)
    m.ajoute(s2)
    m.ajoute(s3)
    m.ajoute(s4)
    m.ajoute(s5)

    for mes in m:
        if "Hello" in mes:
            print(mes)
            mes.estvu()
    
    print("Now printing unread messages:")
    m.messagesNonLus()
    print("length of messagerie:", len(m))
    print(m[2])
    print("Deleting message:", m[2])
    del m[2]
    print("new length of messagerie:", len(m))
    print("updated messagerie:")
    print(m)
    print("Removing messages from number '555'")
    m.effacenum("555")
    print("Updated messagerie:")
    print(m)
