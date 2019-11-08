from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
)


class Constants(BaseConstants):
    name_in_url = 'choice_exp'
    players_per_group = None
    num_rounds = 2

    options = [
      [ # Round 1
         {
            "size": "small",
            "quality": "regular",
            "price": 50
         },
         {
            "size": "large",
            "quality": "regular",
            "price": 100
         }
      ],
      [ # Round 2
         {
            "size": "small",
            "quality": "regular",
            "price": 50
         },
         {
            "size": "small",
            "quality": "premium",
            "price": 100
         }
      ]
   ]


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():
            p.set_options()

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    choice = models.IntegerField(
        choices=[
            [1, "Option A"],
            [2, "Option B"]
        ],
        widget=widgets.RadioSelect
    )

    sizeA = models.StringField()
    sizeB = models.StringField()
    priceA = models.IntegerField()
    priceB = models.IntegerField()
    qualityA = models.StringField()
    qualityB = models.StringField()

    def set_options(self):
        option_a = Constants.choices[self.subsession.round_number - 1][0]
        option_b = Constants.choices[self.subsession.round_number - 1][1]
        self.priceA = option_a["price"]
        self.priceB = option_b["price"]
        self.qualityA = option_a["quality"]
        self.qualityB = option_b["quality"]
        self.sizeA = option_a["size"]
        self.sizeB = option_b["size"]
