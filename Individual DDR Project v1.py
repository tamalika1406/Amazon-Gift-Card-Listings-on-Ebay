from bs4 import BeautifulSoup
import requests
import urllib.parse
import re
import urllib
import time
import glob
import os
import pandas as pd


def part1():
    ## (a) use the URL identified above and write code that loads eBay's search result page
    ## containing sold "amazon gift card". Save the result to file. Give the file the filename "amazon_gift_card_01.htm".
    URL = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=amazon+gift+card&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=&_pgn=1"
    headers = {'User-Agent': 'Mozilla/5.0'}
    page1 = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page1.text, 'lxml')
    with open(f"amazon_gift_card_01.html", "w") as file:
        file.write(page1.text)
        time.sleep(15)

    ## (b) take your code in (a) and write a loop that will download the first 10 pages of search results.
    ## Save each of these pages to "amazon_gift_card_XX.htm" (XX = page number). IMPORTANT: each page request needs
    ## to be followed by a 10 second pause. Please remember, you want your program to mimic your behavior as a human and
    ## help you make good purchasing decisions

    base_link = "https://www.ebay.com/sch/i.html?_from=R40&_nkw=amazon+gift+card&_sacat=0&rt=nc&LH_Sold=1&LH_Complete=&_pgn="
    for i in range(0, 10):
        pages_ten = base_link + str(i + 1)
        response_content = requests.get(pages_ten)
        with open(f"amazon_gift_card_0{i + 1}.html", "w") as file:
            file.write(response_content.text)
            time.sleep(10)

    ## Please note that: all 10 pages are downloaded however only 4 of them were legitimate for me and for the rest of it,
    ## ebay identified my scraping excercise as bot's excercise. I raised the concern on Piazza and professor commented to leave it as is
    ## Hence the results for scraping are skewed as per as many number of pages.

    ## (c) write code that loops through the pages you downloaded in (b), opens and parses them to a Python or
    ## Java xxxxsoup-object.
    ## (d) using your code in (c) and your answer to 1 (g), identify and print to screen the title, price, and shipping
    ## price of each item.

    z = 0
    page_string = ""
    ship_prc = []
    prod_prc = []
    title = []

    for i in range(0, 10):
        with open(f"amazon_gift_card_0{i + 1}.html", "r") as page_html:
            content = page_html.read()
            soup1 = BeautifulSoup(content, 'lxml')
            abc = soup1.select(
                "li.s-item.s-item__pl-on-bottom > div.s-item__wrapper.clearfix > div.s-item__info.clearfix")
            for k in abc:
                # Fetching titles from each product
                prod_title_1 = k.a.find("div", class_="s-item__title")
                title.append(prod_title_1.text)


                # Fetching selling price from each product
                prod_price_1 = k.find("span", class_="s-item__price")
                prod_prc.append(prod_price_1.text)


                # Fetching shipping price from each product
                shipping = k.find("span", class_="s-item__shipping")
                if shipping is not None:
                    value = shipping.text.strip()
                else:
                    value = shipping
                ship = value if value is not None else "0"
                ship_prc.append(ship)
                z = z + 1

                print(z, ":", prod_title_1.text, "\n Selling Price:", prod_price_1.text, "\n Shipping Price:", ship)

    ## (e) using RegEx, identify and print to screen gift cards that sold above face value. e.,
    ## use RegEx to extract the value of a gift card from its title when possible (doesn’t need to work on all titles, > 90%
    ## success rate if sufficient). Next compare a gift card’s value to its price + shipping (free shipping should be
    ## treated as 0).  If value < price + shipping, then a gift card sells above face value.

    face_value_less = []
    numerical_values = []
    selling_list = []
    title_value = []
    shipping_value = []

    for a, b in zip(title, prod_prc):
        # Regex for price present in title
        price_from_title = re.sub(r"(.*?)(\$*?)(\d+)(.*)", r"\3", a)
        title_value.append(price_from_title)


        # Regex for price present in selling price
        selling_upd = re.sub(r"\$(\d+?)\.(\d+)", r"\1", b)
        selling_list.append(selling_upd)

        # Regex for shipping fee
    for item in ship_prc:
        match = re.search(r"\$(\d+\.\d+)", item)
        if match:
            shipping_value.append(match.group(1))
        else:
            shipping_value.append("0")

        # Put all extracted values in a dataframe to do further transformations for face value calculation
    df_tam = pd.DataFrame({'title_value': title_value, 'selling_list': selling_list, 'shipping_value': shipping_value})

        # Remove rows that have text values as they wont contribute to face value calculation as either of the 3 price
    # information not present
    df_final = df_tam.applymap(lambda x: pd.to_numeric(x, errors='coerce'))
    df_final = df_final.dropna()

        # Created a flag column to flag those rows where the face value is lower than actual value
    df_final['flag'] = (df_final['selling_list'] + df_final['shipping_value'] > df_final['title_value']).astype(int)
    print(df_final[df_final['flag'] == 1])

    ## (f) What fraction of Amazon gift cards sells above face value? Why do you think this is the case?

    print("Face value total", df_final[df_final['flag'] == 1].shape[0] / len(df_tam))

    ## 38% are sold above face value in the 4 pages that I scraped. I could think of the below 2 primary reasons for this:
	## First, buying gift cards in ebay even if conventionally expensive probably is a comfortable way for people to get a gift
	## without having to hustle for going to a store, choosing gift or even choosing a gift online. Getting a gift card, even at
	## a higher price makes it easy for people looking to gift or get something delivered. It is comparable to how we end up
	## ordering groceries from instacart - which is typically slightly expensive per item & includes delivery fee but we still
	## order because it gets delivered at our door step & saves the effort of going to a store & selecting items for ourselves

	## Second, I am not entirely sure of how ebay works but sometimes some payment gateways charge a percentage during transactions.
	## Say 1% is charged for secure transaction when a sender transfers money to the merchant. The higher face value probably accounts
	## for that loss on the merchant side


def part2():
    # (a) Following the steps we discussed in class and write code that automatically logs into the website fctables.com
    URL = "https://www.fctables.com/"
    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(URL, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    session_requests = requests.session()
    time.sleep(5)
    res = session_requests.post(URL, data={"login_action": "1", "login_username": "Tam",
                                           "login_password": "Helloworld1234554321!", "user_remeber": "1",
                                           "submit": "1"}, timeout=15)
    cookies = session_requests.cookies.get_dict()
    print(cookies)

    # (b) Verify that you have successfully logged in:
    # use the cookies you received during log in and write code to access
    # https://www.fctables.com/tipster/my_bets/ Links to an external site..Check whether the word “Wolfsburg” appears on the page

    URL2 = "https://www.fctables.com/tipster/my_bets"

    page2 = session_requests.get(URL2, cookies=cookies)
    doc3 = BeautifulSoup(page2.content, 'html.parser')
    text = doc3.text
    word_given = "Wolfsburg"
    match_check = re.search(r"\b" + word_given + r"\b", text)

    # Check if a match was found
    if match_check:
        print("Word '" + word_given + "' is present")
    else:
        print("Word '" + word_given + "' is absent")


if __name__ == '__main__':
    part1()
    part2()
