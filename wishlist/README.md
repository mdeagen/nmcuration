# Curation Project "Wishlist"
This directory is intended for nascent curation jobs, and specifically to pre-process these jobs before they are moved to "In-Progress".

Before moving a project to the "In-Progress" directory:
* Create a sub-directory for the curation job
* Create a Traveler README.md (see below for instructions)
* Identify datasets of interest (including Figure/Table number where applicable)
* If in communication with the author(s), request and obtain raw datasets where applicable

## Creating the "Traveler" for a Curation Job (README.md)
Analogous to a *manufacturing traveler*, this document will accompany the curation project throughout its journey from "Wishlist" to "Completed."

The format of the traveler is a `README.md` markdown file located in the sub-directory for the curation job. The purpose of this file is to document key steps in the curation process (e.g., moving the project between curation stages), as well as any issues/roadblocks encountered along the way. Documentation of issues and roadblocks is valuable information that will help the team continue to improve and streamline the curation process. By titling the document "README.md", Github will automatically display the document when the sub-directory has been opened.

An example format for the Traveler (in markdown format) is:

    CURATION JOB TRAVELER
    
    # AuthName_YYYY [name of sub-directory]

    **Description:** [brief description of curation job and purpose]
    
    ---
    
    **Traveler Created:** 2020-06-03
    
    **Traveler Modified:** 2020-07-05
    
    **Current Status:** *Wishlist*
    
    ---
    
    ## Bibliographic Info [DOI is sufficient if one exists, otherwise provide full info needed to identify dataset]
    
    * DOI: 10.1234/example.123.45 [DOI of publication]
    * DOI: 10.1234/example.123.45.001 [optional additional DOI of e.g., Supporting Info]
    
    ---
    
    ## Datasets of Interest
    
    * Figure 1, Tg vs. Mass Fraction data
    * Figure 2, Stress-strain data
    * Figure 5, Storage and loss modulus data
    
    ---
    
    ## Events
    
    2020-06-03: Added publication, curation project to "Wishlist" directory (M.E.D.)
    
    2020-06-04: Finalized list of figures with datasets of interest (M.E.D.)
    
    2020-06-05: Added project to "In Progress" (M.E.D.)
    
    2020-06-09: Completed Excel template files (M.E.D.)
    
    2020-06-10: Uploaded files to NanoMine successfully, moved project to "Complete" (M.E.D.)
    
    ---
    
    ## Open Issues
    
    ---
    
    ## Closed Issues
    
    ---
    
    ## Sub-directory Contents [Google Drive/Dropbox, not synced with Github]
    
    * `ExampleName_2018_master-template.xlsx`
    * `ExampleName_2018_notebook.Rmd`
    * `/Raw Data/`
    * `/Submission/`
    

## Is a Paper Already in the NanoMine Knowledge Graph?

Given a DOI, you can check whether that paper already resides in the NanoMine Knowledge Graph. 

To check, run the following query on the [NanoMine (QA) SPARQL endpoint](https://qa.materialsmine.org/wi/sparql.html)

    PREFIX sio: <http://semanticscience.org/resource/>
    PREFIX nm: <http://nanomine.org/ns/>

    SELECT DISTINCT ?doi WHERE {
      ?doi sio:hasPart [ a nm:PolymerNanocomposite ] .
      FILTER regex(str(?doi), "SubstringOfDOI")
    }

after replacing *SubstringOfDOI* with all or part of the actual DOI of interest. If a result is returned that matches the DOI, the paper has been fully or partially curated into the NanoMine Knowledge Graph. At this point, one should inspect further to identify what, if any, information still needs to be curated. If no results are returned by the above query, then it is most likely safe to proceed with curation.

## Requesting Raw Datasets from Authors
Raw datasets that generated a figure are preferred over manual/digital extraction of the data from an image of the figure. Requests to the corresponding author of the paper should be made through the NanoMine email alias (contact Marc Palmeri at marc.j.palmeri`at`duke.edu for assistance in composing and sending the first email correspondence).

The corresponding author of a publication, whose contact information is included on either the first or last page of a published article, is typically the leader of the lab that produced the publication. Requests should be respectful of the author's time and specific to the datasets of interest to NanoMine, with the realization that the raw datasets may not have been archived in a repository. The corresponding author may direct you to contact the lead author of the paper, who may or may not still be a member of the research group.

## Links and Resources
* [**List of papers to possibly curate:**](https://docs.google.com/spreadsheets/d/1JIi_GlqX2KqiNfb7EF4cwO30_tDAg96wYxcHctefUJM/edit) Google Sheet with a (non-prioritized) list of papers to potentially curate
* [**Issue tracker spreadsheet:**](https://docs.google.com/spreadsheets/d/1g3nWS48fCwsUAJjBezQFrGWUsNnp0EnDoNpAEAr6lyE/edit#gid=0) Google Sheet with list of issues with already curated samples



