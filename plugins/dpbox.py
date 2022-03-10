def DPBOX(url):
    if "dl.dropbox.com" in url:
        #print("enter1")
        if "?dl=0" in url:
            DPLINK =url.replace("?dl=0","?dl=1")
        elif "?dl=1" in url:
            DPLINK = url
        else:
            DPLINK = f'{url}?dl=1'

    elif "www.dropbox.com" in url:
        #print("enter2")
        DPLINK =url.replace("www.dropbox.com", "dl.dropbox.com")
        #print(DPLINK)
        if "?dl=0" in DPLINK  or  "?dl=1" in DPLINK:
            DPLINK = url.replace("?dl=0", "?dl=1") if "?dl=0" in url else DPLINK
        else:
            
            DPLINK = f'{DPLINK}?dl=1'

    else:
        print("enter 3")
        if "?dl=0" in DPLINK or "?dl=1" in DPLINK:
            DPLINK = url.replace("?dl=0", "?dl=1") if "?dl=0" in url else url
        else:
            DPLINK = f'{DPLINK}?dl=1'
    return DPLINK
