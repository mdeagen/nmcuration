CURATION JOB TRAVELER

# Benes_2018

**Description:** Published article by Benes *et al.* for the Macromolecules **Virtual Issue**

---

**Traveler Created:** 2020-06-03

**Traveler Modified:** 2020-06-09

**Current Status:** *Completed*

---

## Bibliographic Info

* DOI: 10.1021/acs.macromol.8b01204
* SI: https://pubs.acs.org/doi/suppl/10.1021/acs.macromol.8b01204/suppl_file/ma8b01204_si_001.pdf

---

## Datasets of Interest

* Table 4, DMTA results including T_onset
* Figure S3, Storage and loss modulus data

---

## Events

2020-06-02: (Virtually) added publication, curation project to "Wishlist" (M.E.D.)

2020-06-02: Attempted upload of S1 to NanoMine QA (M.E.D.)
* Error related to system not accepting .csv files (see Issue 1)

2020-06-02: Attempted upload of S1 with datafiles manually "Saved As" .xlsx files (M.E.D.)
* Received "Success!" email report

2020-06-03: Added job to "In-Progress" (M.E.D.)

2020-06-04: Made updates to R code (M.E.D.)
* Several updates to variable casting for NA handling (as.character, as.numeric) due to R 4.0 changes
* Added column names (with units) to data frames later exported as supplementary datafiles
* Changed exported datafile format to .xlsx (previously was .csv)

2020-06-04: Ran R code, uploaded curated files to repo (M.E.D.)

2020-06-04: Manually uploaded all samples (S1-S5) to QA NanoMine Uploader (M.E.D.)
* Received 5 "Success!" auto-generated emails (10:26-10:27 AM)

2020-06-04: Moved curation job to "Completed" (M.E.D.)

2020-06-09: E.D. ran into issue while ingesting spreadsheets into RDF (M.E.D.)
* Beneš author name contains Unicode character that causes celery backend to loop (see Issue 2)
* S1 was uploaded twice (as test on 2020-06-02 and as part of complete batch on 2020-06-04)

2020-06-09: Created new dataset and re-uploaded (S1-S5) to NanoMine QA (M.E.D.)
* Received success email reports (7:54-7:56 AM)


---

## Open Issues


---

## Closed Issues

### Issue 1

>job result code: 21
>error messages: [File Error] Missing file! Please include "S1_storage_modulus.csv.xlsx" in your uploads. [File Error] Missing file! Please include "S1_loss_modulus.csv.xlsx" in your uploads.

**Error:** XMLCONV cannot handle .csv files, instead only accepts .xlsx for tabular data.

**Fix:** Changed output in R script for these datafiles to .xlsx instead of .csv. However, .csv is a more compact and standard format for tabular data and should be supported.

### Issue 2
From E.D. to J.M. and S.R. (email)
> When we attempted to ingest the Beneš samples, the celery backend processor looped because the key for the XML was built improperly apparently because of a different interpretation of the unicode character possibly caused by publish or RDF internal processing -- not sure. The fix seems to be to slugify it which should now be handled.  However, the looping is bothersome since the log entries would've eventually filled the disk.  Would you address this somehow to prevent it in the future?  The scenario was that it kept looking for the XML in the NanoMine rest service and failing with 404 because the request didn't properly use utf-8 encoding for the unicode character. The unicode issue should go away now, but the possibility of other issues causing this loop exist.

**Error:** Special character handling during RDF ingest from XML.

**Fix:** Slugify XML keys.


---

## Sub-directory Contents

* `master_template_2020_Benes.xlsx`
* `Benes_2018_notebook.Rmd`
* `Process_Benes_Nanocomposite.xlsx`
* `Process_Benes_Neat.xlsx`
* `Process_Benes_PST_APBMP.xlsx`
* `Process_Benes_PST_PDA.xlsx`
* `Process_Benes_PST_PEI.xlsx`
* `/RawDataFromAuthors/`
* `/SUBMISSION/`
