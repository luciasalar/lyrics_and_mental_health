
import pandas as pd 


dir_path = '/disk/data/share/s1690903/Lyrics_project/'
lyrics_path = 'data/lyrics_hothp_2010s.csv'


class Collect_billboard:
    def __init__(self):
        '''define the main path'''
        self.path = '/disk/data/share/s1690903/Lyrics_project/'
       

    def clean_data(self, lyrics_path):
        file = pd.read_csv(self.path + lyrics_path)
        # we only retain songs with publication year
        file = file.dropna(subset=['year'])
        clean_file = file.dropna(subset=['lyrics'])

        return clean_file


clean = Collect_billboard()
clean_2010 = clean.clean_data('data/lyrics_hothp_2010s.csv')
clean_90s_00s = clean.clean_data('data/lyrics_hothp_2000s_1990s.csv')
clean_80s = clean.clean_data('data/lyrics_hothp_1980s.csv')

combine_1 = pd.concat([clean_2010, clean_90s_00s])
combine_all = pd.concat([combine_1, clean_80s])














