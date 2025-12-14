import pytest
from pyvote.voting.context import Context


class TestContext:

    def test_constructor_when_given_mandatory_arguments_only_expect_to_work(self):
        pop_size = 1000
        context = Context(population_size=pop_size)
        assert context.population_size == pop_size
        assert context.seed is None

    def test_constructor_when_given_all_arguments_expect_to_work(self):
        pop_size = 1000
        seed = 1234
        context = Context(population_size=pop_size, seed=seed)
        assert context.population_size == pop_size
        assert context.seed == seed

    def test_population_size_smaller_0_expect_error(self):
        with pytest.raises(ValueError):
            Context(population_size=-1)
