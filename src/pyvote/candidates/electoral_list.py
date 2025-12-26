import copy

from pyvote.candidates.candidate import Candidate
from pyvote.candidates.eligible_base import EligibleBase


class ElectoralList(EligibleBase):
    """The ElectoralList class models an electoral list. An electoral list allows to get
    vote either for itself or through one of its candidates. In both cases, the list
    gets a vote.

    :param candidates: the candidates part of the electoral list. The order matters as
        first candidates are elected first.
    :raises ValueError: if the list is empty.
    """

    def __init__(self, candidates: list[Candidate]) -> None:
        if len(candidates) == 0:
            raise ValueError("empty candidate list")
        super().__init__()
        self._candidates: list[Candidate] = copy.deepcopy(candidates)
        """The list of candidates part of the list."""
        self._candidates_dict: dict[Candidate, Candidate] = {
            candidate: candidate for candidate in self._candidates
        }
        """The dictionary of the candidates within the list to perform quick lookups for
        candidates and quickly access them."""

    def __len__(self) -> int:
        """Returns the number of candidates in the list."""
        return len(self._candidates)

    def get_vote_candidate(self, candidate: Candidate) -> None:
        """Adds a vote to a specific candidate in the list.

        The list also gets a vote.
        """
        handle: Candidate | None = self._candidates_dict.get(candidate)
        if handle is None:
            raise ValueError(f"{candidate} is not in this list")
        # adds a vote to both the list and the list
        self.get_vote()
        handle.get_vote()

    def get_top(self, proportion: float) -> list[Candidate]:
        """Returns N candidates corresponding to the given proportion of the list.

        The candidates are selected from first to last in the list. It will always
        report N candidates such that N/L <= proportion where L is the length of the
        list, e.g. with a list of 3, no candidate will be reported with proportion ∈
        [0., 1./3.[, the top 1 with proportion ∈ [1./3., 2./3.[, the top 2 with
        proportion ∈ [2./3., 3./3.[ and all candidates with proportion=1.
        :param proportion: the proportion of candidates to return.
        """
        if 0.0 > proportion > 1:
            msg = "proportion must belong [0,1]"
            raise ValueError(msg)

        candidates: list[Candidate] = []
        n_candidates: int = len(self)
        i_candidate: int = 0

        while (
            (i_candidate + 1) / n_candidates
        ) <= proportion and i_candidate < n_candidates:
            candidates.append(self._candidates[i_candidate])
            i_candidate += 1

        return candidates
