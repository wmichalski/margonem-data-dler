import json
import urllib.request
import os
import errno

json_file = open('urls.json')
json_str = json_file.read()
json_data = json.loads(json_str)
json_file.close()

for element in json_data:
    # wyjecie linku z {"nick": url}:
    url = list(element.items())[0][1]

    print("downloading " + url)
    path = url.replace('www.margonem.pl/obrazki/postacie/','')
    path = "bin/" + path

    # tworzymy sciezke do pliku, zeby byla struktura jak w linku
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
    except:
        pass

    # pobieramy plik
    try:
        if not os.path.isfile(path):
            urllib.request.urlretrieve("http://" + url, path)
    except:
        print("failed to download " + url)

    # jesli mamy zenska koncowke, to probujemy pobrac meska
    if url[-5] == 'f':
        
        # zmiana znaku w stringu
        url_list = list(url)
        url_list[-5] = 'm'
        url = ''.join(url_list)

        path = url.replace('www.margonem.pl/obrazki/postacie/','')
        path = "bin/" + path

        try:
            if not os.path.isfile(path):
                urllib.request.urlretrieve("http://" + url, path)
        except:
            print("failed to download " + url)

    # jesli mamy meska koncowke, to probujemy pobrac zenska
    elif url[-5] == 'm':
        
        url_list = list(url)
        url_list[-5] = 'f'
        url = ''.join(url_list)

        path = url.replace('www.margonem.pl/obrazki/postacie/','')
        path = "bin/" + path

        try:
            if not os.path.isfile(path):
                urllib.request.urlretrieve("http://" + url, path)
        except:
            print("failed to download " + url)



