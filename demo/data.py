import pandas as pd


def to_xml(csvfile):
    """Creates 2 .xml files to validate against an .xsd, one 'valid' and one 'invalid'"""
    df = pd.read_csv(csvfile)
    df.to_xml("data/invalid.xml", index=False)
    df.dropna().to_xml("data/valid.xml", index=False)
    return "Created csv files"
