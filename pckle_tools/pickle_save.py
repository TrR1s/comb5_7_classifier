import pickle


def save_pickle(saving_tuple_dict,path_to_fig_file:str):
    with open(path_to_fig_file, 'wb') as f:
        pickle.dump(saving_tuple_dict, f)