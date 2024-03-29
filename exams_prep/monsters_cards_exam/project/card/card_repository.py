from project.card.card import Card


class CardRepository:
    def __init__(self):
        self.count = 0
        self.cards = []

    def add(self, card: Card):
        card_name = card.name
        names = [c.name for  c in self.cards]

        if card_name in names:
            raise ValueError(f'Card {card_name} already exists!')
        self.cards.append(card)
        self.count += 1

    def remove(self, card):
        if card == '':
            raise ValueError('Card cannot be an empty string!')
        card_to_remove = self.find(card) #card name not object
        self.cards.remove(card_to_remove)
        self.count -= 1

    def find(self, name):
        card = [c for c in self.cards if c.name == name][0]
        return card

