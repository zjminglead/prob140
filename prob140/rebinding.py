from .single_variable import *
from .multi_variable import *

from .version import *
from datascience import *


def ProbabilityTable():
	return Table()

def domain(self,*args):
	if len(args) == 1:
		return single_domain(self,args[0])
	return multi_domain(self,*args)

## Binding; still in debate
Table.chart_colors = chart_colors
Table.prob_event = prob_event
Table.event = event
Table.plot_dist = plot_dist
Table.plot_event = plot_event
Table.domain = domain
Table.probability = probability
Table.probability_function = probability_function
Table.normalized = normalized
Table.expected_value = expected_value
Table.variance = variance
Table.sd = sd
Table.toJoint = toJoint

