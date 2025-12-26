from pyvote.candidates.eligible_base import EligibleBase


class TestEligibleBase:
    """A test suite for the EligibleBase class."""

    def test_constructor_expect_0_votes(self):
        eligible_base = EligibleBase()

        assert eligible_base.votes == 0

    def test_get_vote_when_vote_is_0_expect_vote_equal_1(self):
        eligible_base = EligibleBase()

        eligible_base.get_vote()

        assert eligible_base.votes == 1

    def test_reset_when_vote_is_1_expect_vote_equal_0(self):
        eligible_base = EligibleBase()
        eligible_base.get_vote()

        eligible_base.reset()

        assert eligible_base.votes == 0
