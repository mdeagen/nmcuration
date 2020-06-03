# "In Progress" Curation Projects
This directory is intended for curation jobs that are **actively in progress**. By design, this directory should be kept as uncluttered as possible.

Move a sub-directory for a curation job to this directory after:
* A sub-directory has been created in the "Wishlist" directory
* Figures/data of interest to NanoMine have been identified and added to the README.md in the sub-directory
* All raw data has been obtained (in the event that the curator is working with the author(s) of the paper)
* If moving the sub-directory from the "Stalled" or "Revisited" directories, ensure that the issue has been documented in the README.md of the sub-directory

Once all template files and supplementary files have been added to NanoMine (QA), and a "Success!" report has been returned for each fileset, move the sub-directory to the "Completed" directory.

If the curation job encounters a significant roadblock, add a description to the README.md file and move the sub-directory to the "Stalled" directory.

## Links and Resources
* [**NanoMine Uploader**](https://qa.materialsmine.org/nm#/XMLCONV): Excel template to XML converter on the NanoMine QA server

## Overview of "Samples"
Data in the NanoMine Knowledge Graph are linked to unique identifiers (URIs). Materials data in NanoMine (processing information, property measurements, microstructure images, etc.) are linked back to **samples** from a particular **set of experiments**. Identifying and labeling the samples from a particular experiment is the primary task of curation. Not to be confounded with a sample in the field of statistics, which typically include several individuals from a population, in this context a "sample" is a single material entity that was created during the course of an experiment. In design of experiments (DoE) terminology, this equates to an **observational unit**. One or more measurements or observations may have been taken from a given sample. 

Since the early 2000s, a published research article is typically assigned a digital object identifier (**DOI**) when the article is published. Knowing that a sample came from a particular DOI, one can infer certain information about a sample (e.g., authors, equipment used, etc.), but only information held *constant* within the scope of published work. Experiments contain *variables* that have been systematically studied by the authors in order to perform an analysis and/or reveal certain materials behavior across the samples. As a result, the DOI alone is insufficient to uniquely identify a sample within an experiment. A sample is identifiable based on a specific combination of independent variables known in DoE terminology as **experimental factors**. The *minimal subset* of experimental factors that uniquely identifies a particular sample within an experiment, combined with the DOI for that experiment, form the [primary key](https://en.wikipedia.org/wiki/Primary_key) uniquely defining each sample.

In order to avoid repeatedly referring to a list experimental factors to identify a particular sample, we assign **sample labels** that act as [surrogate keys](https://en.wikipedia.org/wiki/Surrogate_key). The *de facto* sample labeling scheme in NanoMine, for a given experiment, is the letter *S* followed by a *whole number* (S1, S2, S3, ...). If the data are collected in a tidy format (a new row for each new observation, and a new column for each new variable), this labeling can be done automatically at the end of data collection (by iterating the label across rows). Samples do not need to follow a logical order for labeling. In some cases, an author may have performed multiple replicates of a sample and reported only the average values. In the absence of raw data, we are limited to what the author has reported. 



