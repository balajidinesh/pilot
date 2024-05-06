import argparse

from user_end import operate_with_args


def main_parser():
    parser = argparse.ArgumentParser(
        description='Run your Collaborative Designer'
    )

    parser.add_argument('-v', '--verbose', action='store_true',
                        help='enable verbose output')

    parser.add_argument('-a', '--api', type=str,
                        help='specify the llava host API address')

    try:
        args = parser.parse_args()

        operate_with_args(
            api=args.api,
            verbose_mode=args.verbose,
        )

    except Exception as e:
        print("Exception at Main module Arg Parser : \n", e)
    # print(args.accumulate(args.integers))


if __name__ == "__main__":
    main_parser()
