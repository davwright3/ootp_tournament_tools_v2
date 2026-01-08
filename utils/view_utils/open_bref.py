import webbrowser

def open_bref(bref_id):
    start_letter = bref_id[0]
    url = f'https://www.baseball-reference.com/players/{start_letter}/{bref_id}.shtml'
    webbrowser.open(url, new=0, autoraise=True)
    return