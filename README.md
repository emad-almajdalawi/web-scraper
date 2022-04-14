# webscraper

**Author:** Emad Almajdalawi

**Date:** 12/4/2022

**Application Vesrsion:** 0.1.0

**Python Verstion:** 3.9.5

**poetry Vesrsion:** 1.1.13

**pytest verstion:**  5.2

**requests verstion** 2.27.1

**bs4 verstion** 0.0.1

## Overview:
An aplication that scraping data from a Wikipedia page using Python and the packages requests and beautifulSoup. It has two functions:
- `get_citations_needed_count`: to count the number of citation-required paragraphs. O(n^2)
- `get_citations_needed_report`: to generate a report including these paragraphs. O(n^2)