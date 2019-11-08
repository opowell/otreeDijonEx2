from .. import models
import otree.api


class Page(otree.api.Page):
   subsession: models.Subsession
   group: models.Group
   player: models.Player
