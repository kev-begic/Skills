import os
import requests
import urllib.parse
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

def publication_list():

    # Modify for current faculty you are retrieving publications from
    str_prof_name = 'dsbaero'

    # Site main directory
    site_directory = 'http://www-personal.umich.edu/~dsbaero/'

    # Modify page you want publications form
    publication_page = 'http://www-personal.umich.edu/~dsbaero/conference.html'
    query_page = requests.get(publication_page)
    query_page_text = query_page.text

    soup = BeautifulSoup(query_page_text, 'html.parser')

    # Clear text file you want to write to
    open('dsbaero-conference-paper-names.txt', 'w').close()

    paper_count = 0

    for article in soup.findAll('li'):

        paper_count += 1

        paper = article.findChild()

        if (paper.name == 'p'):
            paper = paper.find("a")

        if paper is None:
            continue

        with open('dsbaero-conference-paper-names.txt', 'a') as out:
            out.write(str(paper_count) + ' ' + paper.text + '\n\n')

        # Obtain full link for PDF download
        pdf_download = paper.get("href")
        pdf_download = urllib.parse.quote(pdf_download)

        download_string = site_directory + pdf_download

        # Create string for renaming purposes
        rename_pdf = str_prof_name + '-' + str(paper_count)

        download_file(download_string, rename_pdf)
    # endfor lists
# publication_list()

def download_file(download_url, rename_string):
    full_file_placement = os.path.join('/afs/umich.edu/user/b/e/begic/Documents/CAEN_Web_Dev/publication_scrape/files', rename_string)
    urlretrieve(download_url, full_file_placement)
# download_file

publication_list()


        # for paper in soup.findAll('a'):

        #     # Modify if statement based on DOM model used for site
        #     if paper.parent.name == 'li' or paper.parent.name == 'p':

        #         paper_count += 1

        #         # Modify text file you want to print to
        #         with open('dsbaero-conference-paper-names.txt', 'a') as out:
        #             out.write(str(paper_count) + ' ' + paper.text + '\n\n')

        #         # Obtain full link for PDF download
        #         pdf_download = paper.get("href")
        #         # print(pdf_download)
        #         pdf_download = urllib.parse.quote(pdf_download)
        #         # print(pdf_download + '\n')
        #         download_string = site_directory + pdf_download
        #         # Create string for renaming purposes
        #         rename_pdf = str_prof_name + '-' + str(paper_count)

        #         download_file(download_string, rename_pdf)
            #endif
        #endfor papers with links
    #endfor lists
# publication_list()