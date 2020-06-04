CURATION JOB TRAVELER

# Composto_2019

**Description:** Published article by Bailey *et al.* (Composto group) for the Macromolecules **Virtual Issue**

---

**Traveler Created:** 2020-06-04

**Traveler Modified:** 2020-06-04

**Current Status:** *Completed*

---

## Bibliographic Info

* DOI: 10.1021/acs.macromol.8b02646
* SI: https://pubs.acs.org/doi/suppl/10.1021/acs.macromol.8b02646/suppl_file/ma8b02646_si_001.pdf

---

## Datasets of Interest

* Fig 2 (Sheet 3): Diffusivity of polymer vs. NP loading
* Fig 4-5 (Sheet 5): Diffusivity of NPs and viscosity vs. Matrix MW
* Fig S2 (Sheet 7): Tg vs. NP loading and Matrix MW
* Fig S3 (Sheet 8): Xray scattering data
* Fig S5a (Sheet 10): Dielectric spectra vs. NP loading
* Fig S7 (Sheet 12): Dielectric spectra vs. Matrix MW

---

## Events

2020-06-02: (Virtually) added publication, curation job to "Wishlist" (M.E.D.)

2020-06-04: Added job to "In-Progress" (M.E.D.)

2020-06-04: Made updates to R code (M.E.D.)
* Updated column headers for supplementary datafiles
* Changed datafile export from .csv to .xlsx (NOTE: This causes a SIGNIFICANT increase in execution time compared to the efficient `write_csv` function)
* Various edits for NA handling related to R 4.0 changes
* This R code is less efficient than later iterations that used left_join to assemble the dataframe

2020-06-04: Ran R code to generate sample filesets (M.E.D.)

2020-06-04: Received error messages on first attempt at Upload of S1 to QA (M.E.D.)
* Made correction to export formats in R code list(tibble())

2020-06-04: Received error message on second attempt at Upload of S1 to QA (M.E.D.)
* Removed "several hours" from processing step in master_template that was causing the issue
* Note for future schema updates: should be able to accept commonly used terms as reported by authors

2020-06-04: Received new error message on third attempt at Upload of S1 to QA (M.E.D.)
* When FillerComposition is 0, apparently the entire filler section should remain blank
* Removed Filler Info from master template, configured R code to only populate when NP_Loading > 0

2020-06-04: Successful upload of S1 to NanoMine QA (M.E.D.)

2020-06-04: Encountered issue uploading certain filesets to NanoMine QA (M.E.D.)
* Uploader will NOT allow submission of a sample where there is only a template file (and no supplementary datafiles) in the fileset
* This is a clear bug that affected 11 of the 17 samples in this curation job
* S1-4,16,17 have been successfully uploaded, S5-15 await a fix to this bug before they can be uploaded

2020-06-04: Moved curation job to "Stalled" pending bug fix to Uploader on NanoMine QA (M.E.D.)

2020-06-04: Notified B.H., who has fixed bug but is not online yet. Workaround is to submit the template file in the second upload box in addition to the template upload box.

2020-06-04: Returned curation job to "In-Progress"

2020-06-04: Successfully uploaded samples S5-15 to NanoMine QA

2020-06-04: Moved curation job to "Completed"




---

## Open Issues



---

## Closed Issues

### Issue 1
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'value': 'several' is not a valid value of the atomic type 'xs:double', should be a number. [XML Schema Validation Error] Element 'value': 'Celsius' is not a valid value of the atomic type 'xs:double', should be a number. [XML Schema Validation Error] Element 'GlassTransitionTemperature': Missing child element(s). Expected is ( unit )

**Error:** Identified. "Celsius" mapping to Value field of schema template.
**Fix:** list(tibble()) when adding row to mydf, to preserve columns when writing to Excel templates

### Issue 2
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'value': 'several' is not a valid value of the atomic type 'xs:double', should be a number.

**Error:** Identified. Schema unable to accept "several hours" (which was reported by authors) as a processing step.
**Fix:** Removed from master_template. However, such a commonly used term should be accommodated in the future.

### Issue 3
>job result code: 21
>error messages: exception occurred during mass fraction-volume fraction conversion exception: Traceback (most recent call last): File "/apps/nanomine/src/jobs/XMLCONV/code_src/conversion.py", line 292, in conversion mvc.run() File "/apps/nanomine/src/jobs/XMLCONV/code_src/mfvf.py", line 288, in run self.computeFiller() File "/apps/nanomine/src/jobs/XMLCONV/code_src/mfvf.py", line 77, in computeFiller raise LookupError('[Filler Error] FillerComposition is missing.') LookupError: [Filler Error] FillerComposition is missing.

**Error:** Identified. XMLCONV unable to handle edge case where filler composition is 0.
**Fix:** Removed filler info from master_template. Changed R code to only fill out when NP_Loading > 0

### Issue 4
NanoMine Uploader (QA) **not allowing submission** for filesets that contain *only* a template.xlsx and no supplementary datafiles
S1,2,3,4,16,17 were succesfully uploaded
S5-15 (template only) were NOT uploaded

**Error:** Uploader requires at least 1 file in each upload box in order to enable submission
**Workaround:** Upload the template file in each upload box

---

## Sub-directory Contents

* `master_template_2020_Bailey.xlsx`
* `Bailey_2019_notebook.Rmd`
* `/RawDataFromAuthors/`
* `/SUBMISSION/`
