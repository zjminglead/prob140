from collections import OrderedDict

from datascience import Table
import numpy as np
import pandas as pd
import scipy


class MarkovChain:
    """
    A class for representing, simulating, and computing Markov Chains.
    """

    def __init__(self, states, transition_matrix):
        self.states = states
        self.matrix = transition_matrix

    def to_pandas(self):
        """
        Returns the Pandas DataFrame representation of the MarkovChain.
        """
        return pd.DataFrame(
            data=self.matrix,
            index=self.states,
            columns=self.states
        )

    def get_transition_matrix(self, steps=1):
        """
        Returns the transition matrix after n steps as a numpy matrix.

        Parameters
        ----------
        steps : int (optional)
            Number of steps. (default: 1)

        Returns
        -------
        Transition matrix
        """
        return np.linalg.matrix_power(self.matrix, steps)

    def transition_matrix(self, steps=1):
        """
        Returns the transition matrix after n steps visually as a Pandas df.

        Parameters
        ----------
        steps : int (optional)
            Number of steps. (default: 1)

        Returns
        -------
        Pandas DataFrame
        """
        return pd.DataFrame(
            data=self.get_transition_matrix(steps),
            index=self.states,
            columns=self.states
        )

    def distribution(self, starting_condition, steps=1):
        """
        Finds the distribution of states after n steps given a starting
        condition.

        Parameters
        ----------
        starting_condition : state or Table
            The initial distribution or the original state.
        n : integer
            Number of transition steps.

        Returns
        -------
        Table
            Shows the distribution after n steps

        Examples
        --------
        >>> states = make_array('A', 'B')
        >>> transition_matrix = np.array([[0.1, 0.9],
        ...                               [0.8, 0.2]])
        >>> mc = MarkovChain.from_matrix(states, transition_matrix)
        >>> mc.distribution(start)
        State | Probability
        A     | 0.24
        B     | 0.76
        >>> mc.distribution(start, 0)
        State | Probability
        A     | 0.8
        B     | 0.2
        >>> mc.distribution(start, 3)
        State | Probability
        A     | 0.3576
        B     | 0.6424
        """
        states = list(starting_condition.column(0))
        probabilities = starting_condition.column(1)

        n = len(self.states)
        start = np.zeros((n, 1))
        for i in range(n):
            if self.states[i] in states:
                index = states.index(self.states[i])
                start[i, 0] = probabilities[index]
            else:
                start[i, 0] = 0

        probabilities = start.T @ self.get_transition_matrix(steps=steps)
        return Table().states(self.states).probability(probabilities[0])

    def log_prob_of_path(self, starting_condition, path):
        """
        Finds the log-probability of a path given a starting condition.

        May have better precision than `prob_of_path`.

        Parameters
        ----------
        starting_condition : state or Distribution
            If a state, finds the log-probability of the path starting at that
            state. If a Distribution, finds the probability of the path with
            the first element sampled from the Distribution
        path : array
            Array of states

        Returns
        -------
        float
            log of probability

        Examples
        --------
        >>> states = make_array('A', 'B')
        >>> transition_matrix = np.array([[0.1, 0.9],
        ...                               [0.8, 0.2]])
        >>> mc = MarkovChain.from_matrix(states, transition_matrix)
        >>> mc.log_prob_of_path('A', ['A', 'B', 'A'])
        -2.6310891599660815
        >>> start = Table().states(['A', 'B']).probability([0.8, 0.2])
        >>> mc.log_prob_of_path(start, ['A', 'B', 'A'])
        -0.55164761828624576
        """
        states = list(self.states)
        if isinstance(starting_condition, Table):
            first = path[0]
            index = list(starting_condition.column(0)).index(first)
            assert index != -1, 'First path value not found.'
            log_prob = np.log(starting_condition.column(1)[index])
            prev_index = states.index(first)
            i = 1
        else:
            log_prob = np.log(1)
            prev_index = states.index(starting_condition)
            i = 0

        while i < len(path):
            curr_index = states.index(path[i])
            log_prob += np.log(self.matrix[prev_index, curr_index])
            prev_index = curr_index
            i += 1
        return log_prob

    def prob_of_path(self, starting_condition, path):
        """
        Finds the probability of a path given a starting condition

        Parameters
        ----------
        starting_condition : state or Distribution
            If a state, finds the probability of the path starting at that state. If a Distribution,
            finds the probability of the path with the first element sampled from the Distribution
        path : array
            Array of states

        Returns
        -------
        float
            probability

        Examples
        --------
        >>> mc = Table().states(make_array("A", "B")).transition_probability(make_array(0.5, 0.5, 0.3, 0.7)).toMarkovChain()
        >>> mc.prob_of_path('A', make_array('A', 'B','B'))
        0.175
        >>> start = Table().states(make_array("A", "B")).probability(make_array(.8, .2))
        >>> mc.prob_of_path(start, make_array('A', 'A', 'B','B'))
        0.14
        >>> 0.175 * 0.8
        0.14
        """
        states = list(self.states)
        if isinstance(starting_condition, Table):
            first = path[0]
            index = list(starting_condition.column(0)).index(first)
            assert index != -1, 'First path value not found.'
            prob = starting_condition.column(1)[index]
            prev_index = states.index(first)
            i = 1
        else:
            prob = 1
            prev_index = states.index(starting_condition)
            i = 0

        while i < len(path):
            curr_index = states.index(path[i])
            prob += self.matrix[prev_index, curr_index]
            prev_index = curr_index
            i += 1
        return prob

    def simulate_path(self, starting_condition, steps):
        states = list(self.states)
        if isinstance(starting_condition, Table):
            start = starting_condition.sample_from_dist()
        else:
            start = starting_condition

        path = [start]
        for i in range(steps):
            index = states.index(path[-1])
            next_state = np.random.choice(states, p=self.matrix[index])
            path.append(next_state)

        return np.array(path)

    def steady_state(self):
        eigenvector = scipy.linalg.eig(self.matrix, left=True)[1][:, 0]
        probabilities = eigenvector / sum(eigenvector)
        return Table().values(self.states).probability(probabilities)

    def expected_return_time(self):
        steady = self.steady_state()
        expected_return = steady.column(1)
        return Table().values(self.states).with_column(
            'Expected Return Time',
            1 / expected_return
        )

    def _repr_html_(self):
        return self.to_pandas()._repr_html_()

    def __repr__(self):
        return self.to_pandas().__repr__()

    def __str__(self):
        return self.to_pandas().__str__()

    @classmethod
    def from_table(cls, table):
        """
        Constructs a Markov Chain from a Table

        Parameters
        ----------
        table : Table
            A  table with three columns for source state, target state, and
            probability.

        Returns
        -------
        MarkovChain

        Examples
        --------
        >>> table = Table().states(make_array('A', 'B')) \
        ...     .transition_probability(make_array(0.5, 0.5, 0.3, 0.7))
        >>> table
        Source | Target | Probability
        A      | A      | 0.5
        A      | B      | 0.5
        B      | A      | 0.3
        B      | B      | 0.7
        >>> MarkovChain.from_table(table)
             A    B
        A  0.5  0.5
        B  0.3  0.7
        """
        assert table.num_columns == 3, \
               'Must have 3 columns: source, target, probability'
        for prob_sum in table.group(0, collect=sum).column(2):
            assert round(prob_sum, 6) == 1, \
                   'Transition probabilities must sum to 1.'

        # Get a list of the states.
        ordered_set = OrderedDict()
        for row in table.rows:
            ordered_set[row[0]] = 0
        states = list(ordered_set.keys())

        n = len(states)
        transition_matrix = np.zeros((n, n))

        for row in table.rows:
            source = states.index(row[0])
            target = states.index(row[1])
            transition_matrix[source, target] = row[2]
        return cls(states, transition_matrix)

    @classmethod
    def from_transition_function(cls, states, transition_function):
        """
        Constructs a MarkovChain from a transition function.

        Parameters
        ----------
        states : iterable
            List of states.
        transition_function : function
            Bivariate transition function that maps two states to a
            probability.

        Returns
        -------
        MarkovChain

        Examples
        --------
        >>> states = make_array(1, 2)
        >>> def transition(s1, s2):
        ...    if s1 == s2:
        ...        return 0.7
        ...    else:
        ...        return 0.3
             1    2
        1  0.7  0.3
        2  0.3  0.7
        """
        n = len(states)
        transition_matrix = np.zeros((n, n))
        for i in range(n):
            for j in (range(n)):
                transition_matrix[i, j] = transition_function(states[i],
                                                              states[j])
        return cls(states, transition_matrix)

    @classmethod
    def from_matrix(cls, states, transition_matrix):
        """
        Constructs a MarkovChain from a transition matrix.

        Parameters
        ----------
        states : iterable
            List of states.
        transition_matrix : array
            Square transition matrix.

        Returns
        -------
        MarkovChain

        Examples
        --------
        >>> states = [1, 2]
        >>> transition_matrix = np.array([[0.1, 0.9],
        ...                               [0.8, 0.2]])
        >>> MarkovChain.from_matrix(states, transition_matrix)
             1    2
        1  0.1  0.9
        2  0.8  0.2
        """
        return cls(states, transition_matrix)

def to_markov_chain(self):
    return MarkovChain.from_table(self)
