# NanoMine Curation
This repository is dedicated to the curation of published data from the polymer nanocomposites literature into a structured format for NanoMine.

## Links and Resources
* [**Data Science Productivity Tools**](https://www.edx.org/course/data-science-productivity-tools): A free-to-audit course on edX covering RStudio, Git/Github, and Unix/Linux.
* [**WebPlotDigitizer**](https://apps.automeris.io/wpd/): Tool for semi-automated extraction of raw data from plots.
* [**NanoMine Schema**](https://github.com/bingyinh/nanomine-schema/tree/master/xml): XML Schema Definition (.xsd) files containing the full list of terms (refer to *most recent* schema; filenames contain date in MMDDYY format)
* [**NanoMine Excel Template**](https://github.com/bingyinh/nanomine-schema/tree/master/xls-input-forms): Microsoft Excel workbook into which data for a given sample are assembled
* [**Tidy Data**](https://r4ds.had.co.nz/tidy-data.html): Principles for data tidiness laid out in *R for Data Science* by Hadley Wickham
#### Supplementary links related to the Knowledge Graph side of NanoMine
* [**Tetherless World repo for NanoMine**](https://github.com/tetherless-world/nanomine-graph): Ontology and Knowledge Graph approach to data storage (see [nanomine.ttl](https://github.com/tetherless-world/nanomine-graph/blob/master/nanomine.ttl)), using the RDF data model
* [**RDF Primer**](https://www.w3.org/TR/rdf11-primer/): W3C introduction to the RDF data model
* [**NanoMine SPARQL Endpoint**](https://qa.materialsmine.org/wi/sparql.html): Direct querying of RDF data in the NanoMine Knowledge Graph, using the SPARQL query language
* [**Semantic Data Dictionaries**](https://www.mitpressjournals.org/doi/abs/10.1162/dint_a_00058): Developed by our collaborators at RPI, a specification and method for mapping tabular data into RDF format
* [**NanoMine Ontology spreadsheet**](https://docs.google.com/spreadsheets/d/1hDqbUzgJ2menVFhkjAvZs5uWgVoO-lxi7nxOh6W2QiA/): Google Sheet used to collaboratively develop the NanoMine ontology


## Overview of "Samples"
Data in the NanoMine Knowledge Graph are linked to unique identifiers (URIs). Materials data in NanoMine (processing information, property measurements, microstructure images, etc.) are linked back to **samples** from a particular **set of experiments**. Identifying the samples within a particular DOI is the primary task of curation. Not to be confused with samples in the field of statistics, which typically include several individuals from a population, in this context a "sample" is a single material entity that was created during the course of an experiment. In design of experiments (DoE) terminology, this equates to an **observational unit**. One or more measurements or observations may have been taken from a given sample. 

Since the early 2000s, a published research article is typically assigned a digital object identifier (**DOI**) when the article is published. Knowing that a sample came from a particular DOI, one can infer certain information about a sample (e.g., authors, equipment used, etc.), but only information held *constant* within the scope of published work. Experiments contain *variables* that have been systematically studied by the authors in order to perform an analysis and/or reveal certain materials behavior across the samples. As a result, the DOI alone is insufficient to uniquely identify a sample within an experiment. A sample is identifiable based on a specific combination of independent variables known in DoE terminology as **experimental factors**. The *minimal subset* of experimental factors that uniquely identifies a particular sample within an experiment, combined with the DOI for that experiment, form the [primary key](https://en.wikipedia.org/wiki/Primary_key) uniquely defining each sample.

In order to avoid constantly referring to the minimal subset of experimental factors, we assign sample labels that act as [surrogate keys](https://en.wikipedia.org/wiki/Surrogate_key). The *de facto* sample labeling scheme in NanoMine, for a given experiment, is the letter *S* followed by a *whole number* (S1, S2, S3, ...). If the data are collected in a tidy format (a new row for each new observation, and a new column for each new variable), this labeling can be done automatically at the end of data collection (by iterating the label across rows). Samples do not need to follow a logical order for labeling. In some cases, an author may have performed multiple replicates of a sample and reported only the average values. In the absence of raw data, we are limited to what the author has reported. 

## File and Folder Organization
At the moment, we do not have a standard format for organizing files for curation. The primary directory should contain a README.md with the DOI or other information needed in order to identify the set of experiments that the curated data should be linked to. In the README, it would also be useful to include the relevant experimental factors that varied in the experiment. Each "sample" should have its own sub-directory containing the completed Excel template along with any supplemental data files (.csv, .jpg, etc.). It may be helpful to place these within a "Curated" directory to keep these folders separate from the raw data files or any code used to wrangle and prepare data.

## Git Workflow
To collaboratively manage and keep track of changes to curation-related files, the git workflow will be adopted. Raw data tables and the code used to prepare the raw data should be included.


