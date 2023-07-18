import pandas as pd

def run() -> None:
    movies_data_frame = pd.read_html('https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films', extract_links="all")[0]
    movies_data_frame.columns = ['Movie Name', 'Release Year', 'Awards', 'Nominations']
    movies_data_frame = movies_data_frame.drop(columns=['Awards', 'Nominations'])
    movies_data_frame["Directors Name"] = ""
    movies_data_frame["Production Company"] = ""
    movies_data_frame["Budget"] = ""

    for i, j in movies_data_frame.iterrows():
        link = f'https://en.wikipedia.org{j[0][1]}'
        movies_data_frame.iat[i, 0] = j[0][0]
        movies_data_frame.iat[i, 1] = j[1][0]

        try:
            all_movie_data = pd.read_html(link, match=j[0][0])

            for entry in all_movie_data[0].values:
                if entry[0] == 'Directed by':
                    movies_data_frame.iat[i, 2] = entry[1]

                if entry[0] == 'Production company':
                    movies_data_frame.iat[i, 3] = entry[1]

                if entry[0] == 'Budget':
                    movies_data_frame.iat[i, 4] = entry[1]
        except:
            print(f"Cant load movie: {j[0][0]}")

    movies_data_frame.to_csv('data.csv', sep='\t', encoding='utf-8')
    