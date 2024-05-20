import xml.dom.minidom
import xml.sax
from xml.sax.handler import ContentHandler
import matplotlib.pyplot as plt
from datetime import datetime

# Define the XML file path
XML_FILE = '/Users/yun/Desktop/IBInotes/go_obo.xml'  

# Define the ontologies of interest
ONTOLOGIES = {
    'molecular_function': 0,
    'biological_process': 0,
    'cellular_component': 0
}

# SAX ContentHandler to count terms
class GoHandler(ContentHandler):
    def __init__(self):
        self.counts = ONTOLOGIES.copy()
        self.current_data = ""
        self.current_tag = ""

    def startElement(self, tag, attrs):
        self.current_tag = tag

    def characters(self, content):
        if self.current_tag == 'namespace':
            self.current_data = content

    def endElement(self, tag):
        if tag == 'namespace' and self.current_data in self.counts:
            self.counts[self.current_data] += 1
        self.current_data = ""
        self.current_tag = ""

# Function to parse XML using DOM API
def parse_xml_dom(xml_file):
    start_time = datetime.now()
    dom_tree = xml.dom.minidom.parse(xml_file)
    terms = dom_tree.getElementsByTagName('term')
    counts = ONTOLOGIES.copy()

    for term in terms:
        namespace = term.getElementsByTagName('namespace')[0].firstChild.data
        if namespace in counts:
            counts[namespace] += 1

    end_time = datetime.now()
    return counts, end_time - start_time

# Function to parse XML using SAX API
def parse_xml_sax(xml_file):
    start_time = datetime.now()
    parser = xml.sax.make_parser()
    handler = GoHandler()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    end_time = datetime.now()
    return handler.counts, end_time - start_time

# Plot the results
def plot_data(counts, title):
    plt.figure(figsize=(10, 5))
    labels = list(counts.keys())
    counts = list(counts.values())
    plt.bar(labels, counts, color='skyblue')
    plt.xlabel('Ontologies')
    plt.ylabel('Frequency')
    plt.title(title)
    plt.show()
    plt.clf()

def main():
    # Parse XML using DOM
    dom_counts, time_dom = parse_xml_dom(XML_FILE)
    print("Results using DOM:")
    for ontology, count in dom_counts.items():
        print(f"{ontology.capitalize()}: {count}")
    print("Time taken by DOM:", time_dom)

    # Parse XML using SAX
    sax_counts, time_sax = parse_xml_sax(XML_FILE)
    print("\nResults using SAX:")
    for ontology, count in sax_counts.items():
        print(f"{ontology.capitalize()}: {count}")
    print("Time taken by SAX:", time_sax)

    # Determine which API was faster
    if time_dom < time_sax:
        print("\nDOM API was faster.")
    else:
        print("\nSAX API was faster.")

    # Plot the results
    plot_data(dom_counts, 'DOM Parsing Results')
    plot_data(sax_counts, 'SAX Parsing Results')

if __name__ == "__main__":
    main()
