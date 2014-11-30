__author__ = 'sid'

import os
import pickle

import common
from common import *

def getAppDetails(appUrl):
    #if appUrl in apps_discovered: return None
    soup = common.getPageAsSoup(appUrl)
    if not soup:
        return None

    id = ""
    begin = appUrl.rindex("/")
    end = appUrl.index("?mt=")
    if begin != -1 & end != -1:
        id = appUrl[begin + 3:end]

    pTitleDiv = soup.find('p', {'class': 'title'})
    if pTitleDiv and pTitleDiv.getText() == 'One Moment Please.':
        return None

    appDetails = {}
    appDetails['id'] = id
    appDetails['app_url'] = appUrl
    appUpdate = {}

    titleDiv = soup.find( 'div', {'id' : 'title'} )
    appDetails['title'] = titleDiv.find( 'h1' ).getText()
    appDetails['developer'] = titleDiv.find( 'h2' ).getText()


    centerDiv = soup.find( 'div', {'class' : 'center-stack'} )
    if not centerDiv:
        return None

    for prod_review in centerDiv.findAll('div', {'class' : 'product-review'}):
        if 'Description' in prod_review.get('metrics-loc'):
            desc = prod_review.find('p')
            appDetails['description'] = str(desc)
        elif 'What\'s New' in prod_review.get('metrics-loc'):
            whats_new = prod_review.find('p')
            appUpdate['whats_new'] = str(whats_new)

    imageDiv = centerDiv.find('div', {'class' : 'swoosh lockup-container application large screenshots'})
    if imageDiv:
        iPhoneImages = []
        iPadImages = []
        for image in imageDiv.findAll('img'):
            alt = image.get('alt')
            if alt.find("iPhone") == 0:
                iPhoneImages.append(image.get('src'))
            elif alt.find("iPad") == 0:
                iPadImages.append(image.get('src'))
        if len(iPhoneImages) > 0:
            appDetails['iPhoneImages'] = iPhoneImages
        if len(iPadImages) > 0:
            appDetails['iPadImages'] = iPadImages


    detailsDiv = soup.find( 'div', {'id' : 'left-stack'} )
    if not detailsDiv:
        return None

    priceDiv = detailsDiv.find( 'div', {'class' : 'price'} )
    if priceDiv:
        appUpdate['price'] = priceDiv.getText()

    categoryDiv = detailsDiv.find( 'li', {'class' : 'genre'} )
    if categoryDiv:
        appDetails['category'] = categoryDiv.find( 'a' ).getText()
        appDetails['category-url'] = categoryDiv.find( 'a' )['href']

    releaseDateDiv = detailsDiv.find( 'li', {'class' : 'release-date'} )
    if releaseDateDiv:
        releaseDateDiv.span.extract()
        appUpdate['release_date'] = releaseDateDiv.getText()

    versionDiv = releaseDateDiv.find_next_sibling('li')
    if versionDiv:
        versionDiv.span.extract()
        appUpdate['version'] = versionDiv.getText()

    sizeDiv = versionDiv.find_next_sibling('li')
    if sizeDiv:
        sizeDiv.span.extract()
        appUpdate['size'] = sizeDiv.getText()

    languageDiv = detailsDiv.find( 'li', {'class' : 'language'} )
    if languageDiv:
        appDetails['language'] = languageDiv.getText().split()

    contentRatingDiv = detailsDiv.find( 'div', {'class' : 'app-rating'} )
    if contentRatingDiv:
        appDetails['content_rating'] = contentRatingDiv.getText()

    contentRatingReasonDiv = detailsDiv.find('list app-rating-reasons')
    if contentRatingReasonDiv:
        appDetails['content_rating_reason'] = [li.getText() for li in contentRatingReasonDiv.findAll('li')]

    compatibilityDiv = detailsDiv.find( 'p' )
    if compatibilityDiv:
        appDetails['compatibility'] = compatibilityDiv.getText()

    customerRatingDivs = detailsDiv.findAll( 'div', {'class' : 'rating', 'role': 'img'} )
    if customerRatingDivs:
        currentRating = customerRatingDivs[0].get( 'aria-label' ).split( ',' )
        appDetails['rating-current'] = currentRating[0].strip()
        appDetails['rating-current-count'] = currentRating[1].strip()
        customerRating = customerRatingDivs[-1].get( 'aria-label' ).split( ',' )
        appDetails['rating-all'] = customerRating[0].strip()
        appDetails['rating-all-count'] = customerRating[1].strip()
    else:
        appDetails['rating-current'] = 'N/A'
        appDetails['rating-current-count'] = 'N/A'
        appDetails['rating-all'] = 'N/A'
        appDetails['rating-all-count'] = 'N/A'

    iconDiv = detailsDiv.find('div', {'class' : 'artwork'})
    if iconDiv:
        appDetails['icon'] = iconDiv.find('img').get('src')

    appLinksDiv = soup.find( 'div', {'class' : 'app-links'} )
    if appLinksDiv:
        for link in appLinksDiv.findAll( 'a', {'class' : 'see-all'} ):
            text = link.getText()
            href = link.get( 'href' )
            if text.endswith( 'Web Site' ):
                appDetails['developer_website'] = href
            elif text.endswith('Support'):
                appDetails['support'] = href
            elif text.endswith('Agreement'):
                appDetails['license'] = href

    print(appUpdate)
    appDetails['update'] = appUpdate

    #apps_discovered.append( appUrl )
    return appDetails

def dumpApp(app_detail, of):
    if app_detail == None:
        return

    print(app_detail['title'])
    text = u"'title': '" + app_detail['title'] + "'"
    text += ", 'rating': '" + app_detail['rating'] + "'"
    text += ", 'app_url': '" + app_detail['app_url'] + "'"
    text += ", 'description': '" + str(app_detail['description']) + "'"
    text += '\n'
    print(text)
    of.write(bytes(text, 'UTF-8'))

def pickleApp(app_detail):
    if app_detail == None:
        return

    id = app_detail['id']
    with open('./' + DATA_DIR + '/apps/' + id + '.pkl', 'wb') as f:
         pickle.dump(app_detail, f)

def unpickleApp(id):
    with open('./' + DATA_DIR + '/apps/' + id + '.pkl', 'rb') as f:
         return pickle.load(f)

def getAllAppData(cat):
    for name in os.listdir("./" + DATA_DIR):
        if (cat != "") & (name != cat):
            continue

        #print(name)
        name = "./" + DATA_DIR + "/" + name
        if os.path.isdir(name):
            app_url_file = name + "/" + DATA_APP_URL_FILE
            if os.path.exists(app_url_file):
                print(app_url_file)

                count = 0
                app_count_file = name + "/" + DATA_APP_COUNT_FILE
                if os.path.exists(app_count_file):
                    f = open(app_count_file)
                    count = int(f.readline())
                    f.close()

                if count == 0:
                    # create the 1st data file
                    app_data_file = name + "/app_data_0"
                    of = open(app_data_file, 'wb')

                app_count = 0
                f = open(app_url_file)
                for line in f:
                    if count == 0:
                        # create a new data file
                        if app_count % 1000 == 0:
                            of.close()
                            file_index = round(app_count/1000)
                            app_data_file = name + "/app_data_" + str(file_index)
                            of = open(app_data_file, 'wb')

                        app_detail = getAppDetails(line)
                        dumpApp(app_detail, of)
                    else:
                        if app_count == count - 1:
                            file_index = int(app_count/1000)
                            app_data_file = name + "/app_data_" + str(file_index)
                            of = open(app_data_file, 'a+b')
                        elif app_count >= count:
                            # create a new data file
                            if app_count % 1000 == 0:
                                of.close()
                                file_index = round(app_count/1000)
                                app_data_file = name + "/app_data_" + str(file_index)
                                of = open(app_data_file, 'wb')

                            app_detail = getAppDetails(line)
                            dumpApp(app_detail, of)

                    app_count += 1

                of.close()
                f.close()


#app_url = "https://itunes.apple.com/us/app/angry-birds/id343200656?mt=8"
#app_url = "https://itunes.apple.com/us/app/isnowreport/id412841793?mt=8"
#app_url = "https://itunes.apple.com/us/app/appzapp-hd-pro-daily-new-apps/id428248004?mt=8"
#app_url = "https://itunes.apple.com/us/app/aar-planner/id583324413?mt=8"
#app_details = getAppDetails(app_url)
#print(app_details)
#print("'description': '" + str(app_details['description']))

if __name__ == "__main__":
    getAllAppData("")



