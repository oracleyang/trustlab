# -*- coding: utf-8 -*-
"""Models for trust game."""

# <standard imports>
from __future__ import division
from otree.db import models
from otree.constants import BaseConstants
from otree.models import BaseSubsession, BaseGroup, BasePlayer

from otree.common import Currency
# </standard imports>


doc = """
This is a standard 2-player trust game where the amount sent by player 1 gets
tripled. The trust game was first proposed by
<a href="http://econweb.ucsd.edu/~jandreon/Econ264/papers/ \
Berg%20et%20al%20GEB%201995.pdf" target="_blank">
    Berg, Dickhaut, and McCabe (1995)
</a>.
"""


source_code = "https://github.com/oTree-org/oTree/tree/master/trust"
bibliography = ()
links = {}
keywords = ("Trust Game",)


class Constants(BaseConstants):
    """Constants for Trust game."""

    name_in_url = 'trust'
    players_per_group = 2
    num_rounds = 1

    # Initial amount allocated to each player
    amount_allocated = Currency(10)
    multiplication_factor = 3
    bonus = Currency(10)

    training_answer_x_correct = Currency(130)
    training_answer_y_correct = Currency(10)


class Subsession(BaseSubsession):
    """Subsession model for Trust game."""

    def before_session_starts(self):
        """Set treatment of the game (see settings.py) as global var."""
        if 'treatment' in self.session.config:
            self.session.vars['treatment'] = self.session.config['treatment']


class Group(BaseGroup):
    """Group model for Trust game."""

    sent_amount = models.CurrencyField(
        min=0, max=Constants.amount_allocated,
        doc="""Amount sent by P1""",
    )

    sent_back_amount_0 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 0 from P1""",
        min=Currency(0),
    )

    sent_back_amount_1 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 1 from P1""",
        min=Currency(0),
    )

    sent_back_amount_2 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 2 from P1""",
        min=Currency(0),
    )

    sent_back_amount_3 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 3 from P1""",
        min=Currency(0),
    )

    sent_back_amount_4 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 4 from P1""",
        min=Currency(0),
    )

    sent_back_amount_5 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 5 from P1""",
        min=Currency(0),
    )

    sent_back_amount_6 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 6 from P1""",
        min=Currency(0),
    )

    sent_back_amount_7 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 7 from P1""",
        min=Currency(0),
    )

    sent_back_amount_8 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 8 from P1""",
        min=Currency(0),
    )

    sent_back_amount_9 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 9 from P1""",
        min=Currency(0),
    )

    sent_back_amount_10 = models.CurrencyField(
        doc="""Amount sent back by P2 for an contribution of 10 from P1""",
        min=Currency(0),
    )


class Player(BasePlayer):
    """Player model for Trust."""

    email = models.EmailField()

    def role(self):
        """Return role ID/name based on ID in group."""
        return {1: 'A', 2: 'B'}[self.id_in_group]
