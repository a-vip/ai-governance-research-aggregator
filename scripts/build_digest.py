import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET
import datetime

# Define arXiv search query
# Using terms relevant to AI Governance and ethics
KEYWORDS = [
    '"AI Governance"',
    '"Autonomous Weapons"',
    '"Meaningful Human Control"',
    '"AI Policy"',
    '"AI Ethics"',
    '"AI Law"',
    '"Surveillance"'
]
search_query = " OR ".join([f"all:{kw}" for kw in KEYWORDS])
encoded_query = urllib.parse.quote(search_query)

# arXiv API endpoint
url = f'http://export.arxiv.org/api/query?search_query={encoded_query}&sortBy=submittedDate&sortOrder=descending&max_results=10'

def fetch_papers():
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req) as response:
            data = response.read()
        return data
    except Exception as e:
        print(f"Error fetching from arXiv: {e}")
        return None

def parse_xml(xml_data):
    ns = {'atom': 'http://www.w3.org/2005/Atom'}
    root = ET.fromstring(xml_data)
    papers = []
    
    for entry in root.findall('atom:entry', ns):
        title = entry.find('atom:title', ns).text.replace('\n', ' ').strip()
        summary = entry.find('atom:summary', ns).text.replace('\n', ' ').strip()
        link = entry.find("atom:link[@title='pdf']", ns)
        if link is not None:
            pdf_url = link.attrib['href']
        else:
            pdf_url = entry.find("atom:id", ns).text
            
        published = entry.find('atom:published', ns).text
        # Parse date to human readable
        date_obj = datetime.datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
        date_str = date_obj.strftime("%B %d, %Y")
        
        authors = []
        for author in entry.findall('atom:author', ns):
            name = author.find('atom:name', ns).text
            authors.append(name)
            
        papers.append({
            'title': title,
            'summary': summary,
            'pdf_url': pdf_url,
            'date': date_str,
            'authors': ", ".join(authors)
        })
    return papers

def generate_markdown(papers):
    current_date = datetime.datetime.now().strftime("%B %d, %Y")
    
    md_content = f"""# 🤖 AI Governance & Sovereign Algorithms Research Aggregator

<div align="center">
  <p><strong>A continuously updated repository of the latest academic research.</strong></p>
  <p><em>Curated and maintained by <a href="https://aviperera.com">Avi Perera</a></em></p>
  <p>
    <a href="https://aviperera.com">Website</a> •
    <a href="https://twitter.com/aviperera_">Twitter</a> •
    <a href="https://www.researchgate.net/profile/Avi-Perera">ResearchGate</a> •
    <a href="https://orcid.org/0009-0005-1903-6868">ORCID</a>
  </p>
  <hr>
</div>

Welcome to the **AI Governance Research Aggregator**. This resource autonomously queries academic databases every week to compile the latest papers on Artificial Intelligence Policy, Ethics, Lethal Autonomous Weapons Systems (LAWS), Surveillance, and Meaningful Human Control.

*Last Updated: {current_date}*

## 📚 Latest Research Digest

"""
    
    if not papers:
        md_content += "> No new papers found this week.\n\n"
    else:
        for paper in papers:
            md_content += f"### [{paper['title']}]({paper['pdf_url']})\n"
            md_content += f"**Authors:** {paper['authors']} | **Published:** {paper['date']}\n\n"
            md_content += f"> {paper['summary']}\n\n"
            md_content += "---\n\n"
            
    md_content += """
## 🔗 Related Resources & Authority Insights

To dive deeper into the intersection of technology, law, and international security, explore the following curated resources:

*   **[Avi Perera | Official Website](https://aviperera.com)** - Read the latest articles on Sovereign Algorithms and AI Governance.
*   **[Sovereign Dashboard](https://sovdash.com)** - An interactive analysis platform for state-level AI capabilities.
*   **[The LAWS Framework](https://github.com/a-vip/ai-governance-laws-frameworks)** - Legal analysis frameworks regarding artificial intelligence governance.

<br>

<div align="center">
  <small><em>This repository is fully autonomous and powered by GitHub Actions.</em></small><br>
  <small><em>Copyright © Avi Perera. All academic papers belong to their respective authors.</em></small>
</div>
"""
    return md_content

if __name__ == "__main__":
    print("Fetching papers from arXiv...")
    xml_data = fetch_papers()
    if xml_data:
        print("Parsing papers...")
        papers = parse_xml(xml_data)
        print(f"Found {len(papers)} papers. Generating README.md...")
        md = generate_markdown(papers)
        
        with open("README.md", "w", encoding="utf-8") as f:
            f.write(md)
        print("README.md successfully updated!")
    else:
        print("Failed to update README.md due to fetch error.")
