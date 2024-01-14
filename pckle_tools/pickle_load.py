import pickle


def load_pickle(path_to_fig_file:str):
    with open(path_to_fig_file, 'rb') as f:
        load_pickle = pickle.load(f)
    return load_pickle



