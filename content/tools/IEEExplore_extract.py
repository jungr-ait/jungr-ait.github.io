#!/usr/bin/env python3
import csv
import re
import argparse

def create_html_links(csv_file):
    """
    Parses a CSV file containing publication data and generates HTML links 
    in the specified format.

    Args:
        csv_file: The path to the CSV file.

    Returns:
        A string containing the HTML code for the publications.
    """

    html_output = ""

    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.DictReader(file)  # Use DictReader to access columns by header name
        for row in reader:
            # Extract information from the CSV row
            title = row.get('Document Title', 'Title not found') # use get to avoid errors when column is missing
            authors = row.get('Authors', 'Authors not found')
            journal = row.get('Document Identifier', 'Journal not found')
            publication_title = row.get('Publication Title', 'Publ. title not found')
            year = row.get('Publication Year', 'Year not found')

            link = row.get('PDF Link')
            # Attempt to create a link based on the DOI (most reliable method)
            doi = row.get('DOI')
            #link = ""
            #if doi:
            #    link = f"https://doi.org/{doi}"
            #else:
                # Try to create a link based on the title (less reliable)
            #    title_for_link = re.sub(r'[^\w\s-]', '', title).lower().replace(' ', '-') # clean title
            #    link = f"https://scholar.google.com/scholar?q={title_for_link}"

            # Create the HTML link
            html_output += f'<li class="paper"><b><a href="{link}" target="_blank">{title}</a></b><br>'
            html_output += f'{authors}<br>'
            html_output += f'<i>{publication_title} ({journal}), {year}</i></li>\n'

    return html_output


def main():

    parser = argparse.ArgumentParser(
        description='IEEExplore_extract: Extract and convert IEEExplore->Authors Published Works from CSV to HTML')
    parser.add_argument('--csv_file_in', help='CSV file downloaded from IEEExplore',
                        default='')
    parser.add_argument('--html_file_out', help='HTML file with results', default="publications.html")
    
    args = parser.parse_args()
    html_links = create_html_links(args.csv_file_in)
    print(html_links)
    with open(args.html_file_out, 'w', encoding='utf-8') as f:
      f.write(html_links)
    pass
     
     
if __name__ == '__main__':
    main()
    pass
