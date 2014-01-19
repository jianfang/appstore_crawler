__author__ = 'sid'

import os

import common
from common import *

def getAppDetails(appUrl):
    #if appUrl in apps_discovered: return None
    soup = common.getPageAsSoup(appUrl)
    if not soup:
        return None

    pTitleDiv = soup.find('p', {'class': 'title'})
    if pTitleDiv and pTitleDiv.getText() == 'One Moment Please.':
        return None

    appDetails = {}
    appDetails['app_url'] = appUrl

    titleDiv = soup.find( 'div', {'id' : 'title'} )
    appDetails['title'] = titleDiv.find( 'h1' ).getText()
    appDetails['developer'] = titleDiv.find( 'h2' ).getText()


    centerDiv = soup.find( 'div', {'class' : 'center-stack'} )
    if not centerDiv:
        return None

    for prod_review in centerDiv.findAll('div', {'class' : 'product-review'}):
        if 'Description' in prod_review.get('metrics-loc'):
            desc = prod_review.find('p')
            appDetails['description'] = desc
        elif 'What\'s New' in prod_review.get('metrics-loc'):
            whats_new = prod_review.find('p')
            appDetails['whats_new'] = whats_new

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
        appDetails['price'] = priceDiv.getText()

    categoryDiv = detailsDiv.find( 'li', {'class' : 'genre'} )
    if categoryDiv:
        appDetails['category'] = categoryDiv.find( 'a' ).getText()

    releaseDateDiv = detailsDiv.find( 'li', {'class' : 'release-date'} )
    if releaseDateDiv:
        appDetails['release_date'] = releaseDateDiv.getText()

    languageDiv = detailsDiv.find( 'li', {'class' : 'language'} )
    if languageDiv:
        appDetails['language'] = languageDiv.getText().split()

    contentRatingDiv = detailsDiv.find( 'div', {'class' : 'app-rating'} )
    if contentRatingDiv:
        appDetails['content_rating'] = contentRatingDiv.getText()

    contentRatingReasonDiv = detailsDiv.find( 'list app-rating-reasons' )
    if contentRatingReasonDiv:
        appDetails['content_rating_reason'] = [li.getText() for li in contentRatingReasonDiv.findAll( 'li' )]

    compatibilityDiv = detailsDiv.find( 'p' )
    if compatibilityDiv:
        appDetails['compatibility'] = compatibilityDiv.getText()

    customerRatingDivs = detailsDiv.findAll( 'div', {'class' : 'rating', 'role': 'img'} )
    if customerRatingDivs:
        customerRating = customerRatingDivs[-1].get( 'aria-label' ).split( ',' )
        appDetails['rating'] = customerRating[0].strip()
        appDetails['reviewers'] = customerRating[1].strip()

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

    #apps_discovered.append( appUrl )
    return appDetails

def dumpApp(app_detail, of):
    text = u"'title': '" + app_detail['title'] + "'"
    text += '\n'
    print(text)
    of.write(text.encode('utf8'))

def getAllAppData():
    name = ""
    for name in os.listdir("./" + DATA_DIR):
        #print(name)
        name = "./" + DATA_DIR + "/" + name
        if os.path.isdir(name):
            app_url_file = name + "/" + DATA_APP_URL_FILE
            if os.path.exists(app_url_file):
                app_count = 0
                file_index = 0
                # create the 1st data file
                app_data_file = name + "/app_data_" + str(file_index)
                of = open(app_data_file, 'wb')

                print(app_url_file)
                f = open(app_url_file)
                for line in f:
                    # create a new data file
                    if app_count == 1000:
                        of.close()
                        app_count = 0
                        file_index += 1
                        app_data_file = name + "/app_data_" + str(file_index)
                        of = open(app_data_file, 'wb')

                    app_detail = getAppDetails(line)
                    print(app_detail['title'])
                    dumpApp(app_detail, of)
                    app_count += 1
                f.close()

app_url = "https://itunes.apple.com/us/app/angry-birds/id343200656?mt=8"
#app_url = "https://itunes.apple.com/us/app/isnowreport/id412841793?mt=8"
#app_url = "https://itunes.apple.com/us/app/appzapp-hd-pro-daily-new-apps/id428248004?mt=8"
app_details = getAppDetails(app_url)
print(app_details)

#getAllAppData()




