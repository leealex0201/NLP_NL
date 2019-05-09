from Bio import Entrez

def search(query):
	Entrez.email = 'salexlee85@gmail.com'
	handle = Entrez.esearch(db='pubmed',
		sort='relevance',
		retmax='1',
		retmode='xml',
		term=query)
	resutls = Entrez.read(handle)
	return resutls

def fetch_details(id_list):
    ids = ','.join(id_list)
    Entrez.email = 'salexlee85@gmail.com'
    handle = Entrez.efetch(db='pubmed',
                           retmode='xml',
                           id=ids)
    results = Entrez.read(handle)
    return results

if __name__ == '__main__':
    results = search('fever')
    id_list = results['IdList']
    papers = fetch_details(id_list)
    pubmed_article = papers['PubmedArticle']
    element = pubmed_article[0]
    pubmed_data = element['PubmedData']
    medlin_citation = element['MedlineCitation']

    article = medlin_citation['Article']
    
    abstract = article['Abstract']

    abstract_text = abstract['AbstractText']

    for i in abstract_text:
    	print(i)
    	print('####')
    # for i, paper in enumerate(papers):
    #     # print("%d) %s" % (i+1, paper['MedlineCitation']['Article']['ArticleTitle']))
    #     print(papers)
    # Pretty print the first paper in full to observe its structure
    #import json
    #print(json.dumps(papers[0], indent=2, separators=(',', ':')))
