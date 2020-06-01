# NanoMine Curation
This repository is dedicated to curation of published data into a structured format for NanoMine.

## Links and Resources
* [**Data Science Productivity Tools**](https://www.edx.org/course/data-science-productivity-tools): A free-to-audit course on edX covering RStudio, Git/Github, and Unix/Linux.
* [**WebPlotDigitizer**](https://apps.automeris.io/wpd/): Tool for semi-automated extraction of raw data from plots.
* [**NanoMine Schema**](https://github.com/bingyinh/nanomine-schema/tree/master/xml): XML Schema Definition (.xsd) files containing the full list of terms (refer to *most recent* schema; filenames contain date in MMDDYY format)
* [**NanoMine Excel Template**](https://github.com/bingyinh/nanomine-schema/tree/master/xls-input-forms): Microsoft Excel workbook into which data for a given sample are assembled.
* [**Tidy Data**](https://r4ds.had.co.nz/tidy-data.html): Principles for data tidiness laid out in *R for Data Science* by Hadley Wickham
#### Additional Links Related to the Knowledge Graph
* [**Tetherless World repo for NanoMine**](https://github.com/tetherless-world/nanomine-graph): Ontology and Knowledge Graph approach to data storage (see [nanomine.ttl](https://github.com/tetherless-world/nanomine-graph/blob/master/nanomine.ttl)), using the RDF data model
* [**RDF Primer**](https://www.w3.org/TR/rdf11-primer/): W3C introduction to the RDF data model
* [**NanoMine SPARQL Endpoint**](https://qa.materialsmine.org/wi/sparql.html): Direct querying of RDF data in the NanoMine Knowledge Graph, using the SPARQL query language
* [**Semantic Data Dictionaries**](https://www.mitpressjournals.org/doi/abs/10.1162/dint_a_00058): Developed by our collaborators at RPI, a specification and method for mapping tabular data into RDF format


## Overview of "Samples"
Data in the NanoMine Knowledge Graph are linked to unique identifiers (URIs). Materials data (processing information, property measurements, microstructure images, etc.) are derived from **samples** within a particular **set of experiments**. A sample is a single material entity on which multiple measurements may have been taken. 

Published research articles since the early 2000s are assigned a DOI. A DOI is sufficient for inferring information about a sample that remains *fixed* within the published work (e.g., authors, equipment used, etc.), however experiments also contain combinations of *variables* that are unique to each sample. Identifying the samples within a particular DOI is the primary task of curation. The *de facto* sample labeling scheme in NanoMine, for a given experiment, is the letter S followed by a whole number (S1, S2, S3, ...). Samples do not need to follow a logical order for labeling. If the data are collected in a tidy format (a new row for each new observation, and a new column for each new variable), this labeling can be done automatically at the end of data collection (by iterating across rows).

## File and Folder Organization
At the moment, we do not have a standard format for organizing files for curation. The primary directory should contain a README.md with the DOI or other information needed in order to identify the set of experiments that the curated data should be linked to. Each "sample" should have its own sub-directory containing the completed Excel template along with any supplemental data files (.csv, .jpg, etc.).


