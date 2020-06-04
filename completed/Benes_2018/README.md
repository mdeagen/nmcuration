CURATION JOB TRAVELER

# Benes_2018

**Description:** Published article by Benes *et al.* for the Macromolecules **Virtual Issue**

---

**Traveler Created:** 2020-06-03

**Traveler Modified:** 2020-06-04

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

2020-06-03: Added job to "In-Progress" (M.E.D.)

2020-06-04: Made updates to R code (M.E.D.)
* Several updates to variable casting for NA handling (as.character, as.numeric) due to R 4.0 changes
* Added column names (with units) to data frames later exported as supplementary datafiles
* Changed exported datafile format to .xlsx (previously was .csv)

2020-06-04: Ran R code, uploaded curated files to repo (M.E.D.)

2020-06-04: Manually uploaded all samples (S1-S5) to QA NanoMine Uploader (M.E.D.)
* Received 5 "Success!" auto-generated emails (10:26-10:27 AM)

2020-06-04: Moved curation job to "Completed" (M.E.D.)



---

## Open Issues

---

## Closed Issues

>job result code: 21
>error messages: [File Error] Missing file! Please include "S1_storage_modulus.csv.xlsx" in your uploads. [File Error] Missing file! Please include "S1_loss_modulus.csv.xlsx" in your uploads.

**Error:** XMLCONV cannot handle .csv files, instead only accepts .xlsx for tabular data
**Fix:** Changed output in R script for these datafiles to .xlsx instead of .csv. However, .csv is a more compact and standard format for tabular data and should be supported.

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
