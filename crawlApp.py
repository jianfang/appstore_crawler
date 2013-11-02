__author__ = 'sid'

import urllib.request
from bs4 import BeautifulSoup


def getPageAsSoup(url):
    try:
        response = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        print("HTTPError with: ", url, e)
        return None
    the_page = response.read()
    soup = BeautifulSoup(the_page)

    return soup


def getAppDetails(appUrl):
    #if appUrl in apps_discovered: return None
    soup = getPageAsSoup(appUrl)
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

app_url = "https://itunes.apple.com/us/app/angry-birds/id343200656?mt=8"
app_details = getAppDetails(app_url)
print(app_details)





