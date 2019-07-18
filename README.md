# Scraping Beatport

Beatport is a top destination for DJs and producers alike to purchase electronic dance music.

This is a simple scrapy project to get information of the Top 100 tracks (https://www.beatport.com/top-100)

## Extracted data

This project extracts the following:

1. Song title
2. Remix Version
3. Genre
4. Artist
5. Link
6. Release Date
7. Price

title|remix|genre|artist|link|release date|price
-|-|-|-|-|-|-
Big Love|David Penn Extended Remix|House|Pete Heller's Big Love|https://www.beatport.com/artist/pete-hellers-big-love/203551|2019-07-05|1.99
The General|Original Mix|Tech House|Mark Knight|https://www.beatport.com/artist/mark-knight/1938|2019-06-21|2.49
You Little Beauty|Extended|Tech House|FISHER (OZ)|https://www.beatport.com/artist/fisher-oz/628537|2019-05-10|2.49

## Running the spider

You can run the spider using the `scrapy crawl` command:

    $ scrapy crawl beatport_spider

A csv file titled 'beatport.csv' will be generated in the 'spiders' folder.

## Requirements

* Python
* Scrapy
