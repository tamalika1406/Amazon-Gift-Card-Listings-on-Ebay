# Amazon-Gift-Card-Listings-on-Ebay
## Focus: Scraping Amazon Gift Card Listings on Ebay using BeautifulSoup & Selenium

In the digital age, online marketplaces like eBay have become a hub for buying and selling various products, including gift cards. However, identifying the true value of these gift cards and making informed purchasing decisions can be challenging for buyers. Our goal is to develop a web scraping solution that utilizes Selenium and BeautifulSoup to extract and analyze eBay's sold "amazon gift card" listings. By automating the process of gathering data from the search results, we aim to provide valuable insights to buyers and maximize their profitability.

To begin, we will create code that navigates to the specified URL and retrieves the search result page for sold "amazon gift card" listings. The obtained data will be saved in separate files, with the first page saved as "amazon_gift_card_01.htm". To ensure accuracy and mimic human behavior, we will implement a loop that downloads the first 10 pages of search results, incorporating a 10-second pause after each page request.

Next, we will parse the downloaded pages using BeautifulSoup, enabling us to extract crucial information such as the title, price, and shipping cost of each listed gift card. By combining this data with our solution to a previous question involving RegEx, we will identify gift cards that sold above face value. Through careful analysis and comparison of the gift card value extracted from their titles with their respective prices and shipping costs, we can determine whether a gift card sells above face value.

Our automated analysis will provide insights into the fraction or percentage of Amazon gift cards that sell above face value, allowing buyers to make data-driven decisions. Additionally, we will explore the reasons behind this observation, providing a deeper understanding of the factors influencing gift card pricing on eBay.

By leveraging web scraping and automated data analysis, our solution empowers buyers with valuable information, helping them navigate the complex marketplace of sold "Amazon gift card" listings on eBay. This data-driven approach enables users to make informed purchasing decisions, maximize profitability, and gain a competitive edge in the online marketplace

![image](https://github.com/tamalika1406/Amazon-Gift-Card-Listings-on-Ebay/assets/20097878/675c72a3-4686-4064-8cc4-06380aab2a56)
