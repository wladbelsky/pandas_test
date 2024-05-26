import pandas as pd

__all__ = ['load_data', 'count_actions', 'filter_data', 'analyze_client_behavior', 'save_processed_data']


def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)


def count_actions(data: pd.DataFrame) -> pd.DataFrame:
    return data.groupby('client_id').size().reset_index(name='actions_count')


def filter_data(data: pd.DataFrame, action: str) -> pd.DataFrame:
    return data[data['action'] == action]


def analyze_client_behavior(data: pd.DataFrame) -> (float, pd.DataFrame):
    mean_actions = data.groupby('client_id').size().mean()
    top_5_clients = data.groupby('client_id').size().sort_values(ascending=False).head(5)
    return mean_actions, top_5_clients.to_frame('actions_count')


def save_processed_data(data: pd.DataFrame, output_file: str):
    data.to_csv(output_file, index=True)
