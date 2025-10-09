import xmltodict
import pandas as pd
import datetime

def get_ce_doi(parsed_data):
    dois = []

    items = parsed_data.get('bibdataset', {}).get('item', [])

    if not isinstance(items, list):
        items = [items]

    for item in items:
        bibrecord = item.get('bibrecord', {})
        item_info = bibrecord.get('item-info', {})
        itemidlist = item_info.get('itemidlist', {})

        # Extract ce:doi
        doi = itemidlist.get('ce:doi')
        if doi:
            dois.append(doi)

    return dois

def get_publication_date(parsed_data):
    publication_dates = []
    items = parsed_data['bibdataset']['item']
    # Handle single item or list of items
    if not isinstance(items, list):
        items = [items]

    for item in items:
        try:
            date_sort = item['ait:process-info']['ait:date-sort']
            year = date_sort['@year']
            month = date_sort['@month']
            day = date_sort['@day']
            publication_dates.append(f"{year}-{month.zfill(2)}-{day.zfill(2)}")
        except (KeyError, TypeError):
            continue

    return publication_dates


def get_all_titletexts(parsed_data):
    """Extract all title texts from the XML dictionary structure"""
    titles = []
    try:
        items = parsed_data['bibdataset']['item']
        # Handle single item or list of items
        if not isinstance(items, list):
            items = [items]

        for item in items:
            try:
                title_text = item['bibrecord']['head']['citation-title']['titletext']['#text']
                titles.append(title_text)
            except (KeyError, TypeError):
                continue

    except (KeyError, TypeError):
        pass

    return titles


def get_all_ce_paras(parsed_data):
    """Extract all ce:para texts from the XML dictionary structure"""
    paras = []
    try:
        items = parsed_data['bibdataset']['item']
        # Handle single item or list of items
        if not isinstance(items, list):
            items = [items]

        for item in items:
            try:
                ce_para = item['bibrecord']['head']['abstracts']['abstract']['ce:para']
                paras.append(ce_para)
            except (KeyError, TypeError):
                continue

    except (KeyError, TypeError):
        pass

    return paras

def structure_data():
    xml_file_path = '/Users/axeeeeeee/Downloads/xml_files/studies.xml'
    with open(xml_file_path, 'r') as f:
        data = f.read()
        parsed_data = xmltodict.parse(data)

        print('axe_parsed_data: ', parsed_data)
        print('-----------')
        print('-----------')

        get_ce_doi_response = get_ce_doi(parsed_data)
        get_publication_dates_response = get_publication_date(parsed_data)
        get_all_titletexts_response = get_all_titletexts(parsed_data)
        get_all_ce_paras_response = get_all_ce_paras(parsed_data)


        data_dict = {
            'doi': get_ce_doi_response,
            'publication_date': get_publication_dates_response,
            'titles': get_all_titletexts_response,
            'abstract': get_all_ce_paras_response
        }

        df = pd.DataFrame(data_dict)
        if 'publication_date' in df.columns:
            df['publication_date'] = pd.to_datetime(df['publication_date'], format='%Y-%m-%d', errors='coerce')

        return df


print(structure_data())

