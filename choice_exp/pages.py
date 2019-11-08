from ._builtin import Page


class DecidePage(Page):
   form_model = 'player'
   form_fields = ['choice']


page_sequence = [DecidePage]

