import argparse
import sys

def get_max_calories(inputfile : str) -> int:
    _max = 0
    _accumulator = 0
    with open(inputfile) as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                _max = max(_accumulator, _max)
                _accumulator = 0
            else:
                _accumulator += int(line)

    return _max

def get_n_max_calories(inputfile : str, n: int) -> list[int]:
    _topN = []
    _accumulator = 0
    with open(inputfile) as f:
        for line in f:
            line = line.rstrip()
            if line == "":
                _inserted = False
                for _i in range(len(_topN)):
                    if _accumulator > _topN[_i]:
                        _topN.insert(_i, _accumulator)
                        _inserted = True
                        break
                if not _inserted and len(_topN) < n:
                    _topN.append(_accumulator)
                
                if len(_topN) > n:
                    _topN.pop()

                _accumulator = 0
            else:
                _accumulator += int(line)

    return _topN

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename')
    args = parser.parse_args()

    # max_calories = get_max_calories(args.filename)
    # print(f"Max calories: {max_calories}")

    top_3_calories = get_n_max_calories(args.filename, 3)
    print(f"Top 3 calories: {top_3_calories}")
    _total = sum(top_3_calories)
    print(f"Total: {_total}")


    sys.exit(0)

