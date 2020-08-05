CURATION JOB TRAVELER

# Bera_2011_TActa

**Description:** Published article by Bera et al., which includes Tg data of interest.

---

**Traveler Created:** 2020-07-22

**Traveler Modified:** 2020-07-30

**Current Status:** *Wishlist*

---

## Bibliographic Info

* DOI: 10.1016/j.tca.2010.12.006

---

## Datasets of Interest

* Table 1: Tonset of degradation
* Fig 5: DSC curves (arbitrary y-axis placement OK) + Tg (labels) and wt% (see legend)


---

## Events

2020-07-22: Added curation job to "Wishlist" (M.E.D.)
* Added list of datasets of interest

2020-07-24: Added Tidy Table to Repo (H.D.)
* Included Tidy Table in repo and included "Separate Datafiles" file as well

2020-07-24: Removed Fig 6 from datasets of interest (M.E.D.)
* All info in Fig 6 is contained in Fig 5 (labels & legend)

2020-07-29: Added the code and Submissions to repo (H.D.)
* Included the python code
* Added "Submissions" folder

2020-07-30: Finalized code and Submissions (H.D.)
* Fixed bugs with the original code
* Added the "Separate Datafiles" to the "SUBMISSION" folders

2020-07-30: Attempted upload of S1 to QA (M.E.D.)
* Bug in QA uploader (See Issue 1)
* Notified T.F. and A.J.

2020-07-31: T.F. and A.J. identified issue and reverted changes to NanoMine QA Uploader
* Closed Issue 1

2020-08-05: Attempted upload of S1 (M.E.D.)
* Received error 9:39 AM (see Issue 2)

---

## Open Issues

### Issue 2
>Unfortunately, your conversion job xmlconv-cjxFmSiUauanisVNG1H9FE was not successful.
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'Polydispersity': 'Polydispersity index (Mw/Mn) of 2.5' is not a valid value of the atomic type 'PolydispersityType'

**Error:** Sheet "2. Material Types" of `Bera_2011_Master_Template.xlsx` includes "Polydispersity index (Mw/Mn) of 2.5" and instead should just be "2.5" in cell B16.
**Fix:** 

---

## Closed Issues

### Issue 1
> Curation uploader not accepting `.xlsx` file extensions by default
> If changed to "All Files (.*)" the .xlsx will not upload

**Error:** System should accept data files in .xlsx format (error was related to updates to xml-conv that were intended only for MCR tools updates)
**Fix:** Implemented

---

## Sub-directory Contents

* `master_template.xlsx`
* `_notebook.Rmd`
* `/RawDataFromAuthors/`
* `/Images/`
* `/SUBMISSION/`
