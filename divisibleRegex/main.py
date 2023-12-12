import re

from fsmCreatorHelpers import compute_finite_state_machine_for
from fsmToRegexHelpers import compute_regex_from_fsm
from utils import to_binary


def regex_divisible_by(n: int) -> str:
    fsm = compute_finite_state_machine_for(n)
    regex = compute_regex_from_fsm(fsm)
    return regex


def __test():
    n = 3
    __result = regex_divisible_by(n)
    print(__result)
    for i in range(1, 10000):
        match = re.search(__result, to_binary(i))
        if i % n == 0 and match is None:
            print("Your result for n=" + str(n) + " was incorrect when matched against " + str(
                i) + ": False should equal True")
        if i % n != 0 and match is not None:
            print("Your result for n=" + str(n) + " was incorrect when matched against " + str(
                i) + ": True should equal False")


if __name__ == '__main__':
    pattern = '$Spain^'
    string = 'Spain'
    print(re.search(pattern, string))
