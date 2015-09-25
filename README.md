# dblp publication scraper
A scraper that downloads search results from DBLP. You can search for any list of keywords.

Scraping dblp is allowed by them and they even offer an API for it. The API, however, is restricted to the search for authors. 
This is why I wrote this scraper, which allows you to also search for publications. 

## Installation

Just type "pip install dblp" in your terminal and it will get installed. You can also clone this repository and type "python setup.py install" after switching to the downloaded folder.

## How to use it?

After importing it, you can use the search()-function to search in dblp for any array of key words. The result will be a pandas DataFrame.

## Example

Imagine you are interested research in Collaborative Writing and want to evaluate which conferences people who write about it publish to. 
With this library you get a table for every search request, so you can easily compare results. Below is an example for one of these tables 
and the lookup for the search phrase "Collaborative Writing".

```python
import dblp

results = dblp.search(["Collaborative Writing"])

results.head()
```
The Code above yields the following results:


|Authors                 | Link                 | Title                            |Type         | Where    |Year |
|------------------------|:--------------------:|:--------------------------------:|:-----------:|:--------:|----:|
| [Lekha Limbu, Lina M...| http://dx.doi.org/...|How do learners experience join...|article      |Compute...|2015 |
| [Sebastian Gehrmann,...| http://dx.acm.org/...|Deploying AI Methods to Support...|inproceedings|CHI Ext...|2015 |
| [Dakuo Wang, Judith ...| http://dx.acm.org/...|DocuViz: Visualizing Collaborat...|inproceedings|CHI       |2015 |
| [Oluwabunmi Adewoyin...| http://dx.doi.org/...|Exploiting the Use of Wikis to ...|inproceedings|CRIWG     |2015 |
| [Menghui Li, Young M...| http://dx.doi.org/...|An Exploration of Mobile Collab...|inproceedings|HCI (24...|2015 |

Now imagine, you want to look for the papers with "AI" in the title. You can easily do that using pandas:

```python
results[results['Title'].str.contains("AI")]
```

Given the search query above, this yield one paper with the following link: http://doi.acm.org/10.1145/2702613.2732705   

## Licence

This code is published under the MIT licence. Feel free to improve and redistribute my code. I hope I made your life a little bit easier. 
