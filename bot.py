import torch
from utils import sample, predict
from model import CharRNN

def start_text(start_text, n_words = 250):
    # Here we have loaded in a model that trained over 20 epochs `rnn_20_epoch.net`
    with open('saved_model/rnn_20_epoch.net', 'rb') as f:
        checkpoint = torch.load(f)
        
    loaded = CharRNN(checkpoint['tokens'], n_hidden=checkpoint['n_hidden'], n_layers=checkpoint['n_layers'])
    loaded.load_state_dict(checkpoint['state_dict'])

    generated_text = sample(loaded, n_words, top_k=5, prime='{} '.format(start_text))

    generated_text = generated_text.replace('\n', ' ')
    generated_text = '{}.'.format(generated_text.split('.')[0])

    return generated_text

