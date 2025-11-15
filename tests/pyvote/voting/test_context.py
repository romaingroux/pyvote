import pytest

from pyvote.voting.context import Context


class TestContext:

    def test_constructor_when_given_mandatory_arguments_only_expect_to_work(self):
        context = Context(population_size=1000)
        assert context.population_size == 1000
        assert context.seed is None

    def test_constructor_when_given_all_arguments_expect_to_work(self):
        context = Context(population_size=1000, seed=1234)
        assert context.population_size == 1000
        assert context.seed == 1234
        
    def test_population_size_smaller_0_expect_error(self):
        with pytest.raises(ValueError):
            Context(population_size=-1)