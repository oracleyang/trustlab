from otree.api import Currency as c, currency_range
from . import models
from ._builtin import Page, WaitPage
from .models import Constants


class CheckIfRedirect(Page):

    def vars_for_template(self):
        return {
            'global_time_start': self.participant.vars['global_time_start'],
            'global_time_stop': self.participant.vars['global_time_stop'],
            'threshold': self.session.config['speedsters_threshold'],
            'speedsters_redirection': (
                self.session.config['quota_redirects']['speedster']
            ),
            'label': self.participant.label,
            'lang': self.session.vars['lang'],
        }


page_sequence = [
    CheckIfRedirect,
]
