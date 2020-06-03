# "Completed" Curation Projects
Move the sub-directory for a curation job to this directory after:
* The job sub-directory has resided in the "In-Progress" directory
* Excel templates have been generated for each "sample" in the publication
* A "dataset" for the job has been initialized using the NanoMine Uploader (QA)
* The "filesets" have been uploaded to NanoMine (QA)
* A "Success!" report has been received for each uploaded fileset

Once a sub-directory in the "Completed" directory is confirmed to reside on the NanoMine production website, configure git to ignore the raw data files (but keep any *R* code (.Rmd) the Traveler (README.md), and optionally the master Excel template if used). 

## Links and Resources
* [**NanoMine Uploader**](https://qa.materialsmine.org/nm#/XMLCONV): Excel template to XML converter on the NanoMine QA server

## Notes (Pending Updates/Bug Fixes)
* Supplementary datafiles must be .xlsx format (the XML converter does not yet accept .csv)
* When uploading multiple additional files, all must be selected in the Windows Explorer pop-up (therefore, keep all supplementary files to upload in the same directory)


