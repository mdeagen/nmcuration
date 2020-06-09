CURATION JOB TRAVELER

# Jimenez_2019

**Description:** Published article by Ning *et al.* for the Macromolecules **Virtual Issue**

---

**Traveler Created:** 2020-06-05

**Traveler Modified:** 2020-06-05

**Current Status:** *Completed*

---

## Bibliographic Info

* DOI: 10.1021/acs.macromol.9b01380
* SI: https://pubs.acs.org/doi/suppl/10.1021/acs.macromol.9b01380/suppl_file/ma9b01380_si_001.pdf

---

## Datasets of Interest

* Fig 6: Crystallization temp vs. volume fraction PEO matrix
* Fig 7b: Half-life of crystallization vs. crystallization temp
* Fig 8b,c: Crystallization rate, degree of crystallinity vs. volume fraction PEO
* Fig 4a-d: SAXS results (graft density = NA,low,med,high; NP loading = 1.2,3.0,4.8,7.4,11,16 vol%)
* Fig 10a,b: SAXS results (graft density = low,med,high; NP loading = 6.7 vol%; crystallization temp = 58C)

---

## Events

2020-06-02: (Virtually) added publication, curation job to "Wishlist" (M.E.D.)

2020-06-05: Added datasets of interest (M.E.D.)

2020-06-05: Added job to "In-Progress" (M.E.D.)

2020-06-09: Updated R code (M.E.D.)
* output datafiles as .xlsx (instead of .csv as previously)
* datatype fixes related to R 4.0 upgrade

2020-06-09: Ran R code, generated sample filesets (M.E.D.)

2020-06-09: Attempted upload of S1 to QA (M.E.D.)
* Excel template only (earlier issue requiring additional datafiles has been fixed)
* Received "success" email (3:43 PM)

2020-06-09: Attempted uploaded remaining samples S2-S104 (M.E.D.)
* Successful upload of S2-S16 (3:45-3:49 PM)
* Received error from S17 (3:49 PM) (see Issue 1)

2020-06-09: Updated R code, regenerated S17-S104 (M.E.D.)
* Added Boolean condition before printing to Excel (issue caused by two mappings for Crystallization Temperature)

2020-06-09: Attempted upload remaining samples S17-S104 (M.E.D.)
* Received "success" email for S17-S79 (4:07-4:26 PM)
* Received error for S80 (see Issue 2)

2020-06-09: Updated R code, regenerated filesets (M.E.D.)
* Fixed Issue 2

2020-06-09: Attempted upload remaining samples S80-S104 (M.E.D.)
* Received "success" email for S80-S103 (4:36-4:43 PM)
* S104 contained 20 images (fileset is 80.2 MB) and required ~2.5 min to upload
* Received "success" email for S104 (4:47 PM)

2020-06-09: Moved curation job to "Completed" (M.E.D.)




---

## Open Issues




---

## Closed Issues

### Issue 1
>Unfortunately, your conversion job xmlconv-q7nVhYr5z5Qs87dHaEWk2A was not successful.
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'unit': This element is not expected. Expected is one of ( description, value )

**Error:** Crystallization temperature prints unit "Celsius" when there is not a value for crystallization temperature.

**Fix:** Added additional Boolean condition in R code before writing to Excel template

### Issue 2
>Unfortunately, your conversion job xmlconv-gSrDxPMZWJ5rxdN37DNcWw was not successful.
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'value': [facet 'minExclusive'] The value '0.0' must be greater than '0' [XML Schema Validation Error] Element 'value': '0.0' is not a valid value of the atomic type 'PositiveValueType'

**Error:** Graft density of 0.0 was printing (and schema requires positive value)

**Fix:** Replaced instances of graftdens==0 with NA in R dataframe


---

## Sub-directory Contents

* `master_template_2020_Jimenez.xlsx`
* `Jimenez_2019_notebook.Rmd`
* `Nanocomposite_processing_Jimenez.xlsx`
* `PST_processing_Jimenez.xlsx`
* `/RawDataFromAuthors/`
* `/Images/`
* `/SUBMISSION/`
