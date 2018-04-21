
from model import model
from viterbi import viterbi

import argparse

# Parse CLI arguments
args_parser = argparse.ArgumentParser(
	formatter_class = argparse.ArgumentDefaultsHelpFormatter
)

args_parser.add_argument(
	"model_path",
	type = str,
	help = "JSON model definition file path"
)

args_parser.add_argument(
    "observations",
    type = str,
    nargs = "+",
    help = "Sequence of observations (emitted symbols)"
)

args = args_parser.parse_args()

# Run Viterbi algorithm
m = model(args.model_path)
o = args.observations

state_sequence = viterbi(o, m)
print(state_sequence)
