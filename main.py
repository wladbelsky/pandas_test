from argparse import ArgumentParser
from funcs import *


def main():
    parser = ArgumentParser()
    parser.add_argument('--in', '-i', dest='input_file', type=str, help='Path to the input file')
    parser.add_argument('--out_folder', '-o', type=str, help='Path to the output file')
    args = parser.parse_args()
    df = load_data(args.input_file)
    actions_count = count_actions(df)
    filtered_data = filter_data(df, 'purchase')
    mean_actions, top_5_clients = analyze_client_behavior(df)

    save_processed_data(actions_count, f'{args.out_folder}/actions_count.csv')
    save_processed_data(filtered_data, f'{args.out_folder}/filtered_data.csv')
    save_processed_data(top_5_clients, f'{args.out_folder}/top_5_clients.csv')
    with open(f'{args.out_folder}/mean_actions.txt', 'w') as f:
        f.write(str(mean_actions))


if __name__ == '__main__':
    main()
