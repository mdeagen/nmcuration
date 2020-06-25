CURATION JOB TRAVELER

# Mortezaei_2011_CompSciTech

**Description:** Published article by Mortezaei *et al.* on silica/polystyrene nanocomposites.

---

**Traveler Created:** 2020-06-22

**Traveler Modified:** 2020-06-24

**Current Status:** *In-Progress*

---

## Bibliographic Info

* DOI: 10.1016/j.compscitech.2011.02.012

---

## Datasets of Interest

* Table 1: for reference, list of encodings used to describe samples
* Fig 1a-c: DMA data (storage mod, loss mod, tan delta) as a function of temperature (untreated silica)
* Fig 2a-c: DMA data (storage mod, loss mod, tan delta) as a function of temperature (treated silica)
* Fig 4a-c: DMA data (storage mod, loss mod, tan delta) as a function of frequency (treated and untreated silica)
> Glass-transition of pure polystyrene is around 102 °C and shift to 103, 105, 107 and 110 °C for the untreated silica content of 0.5%, 1.5%, 2.5% and 5.0%, respectively.
* Estimate Tg of treated polystyrene samples (Based on tan delta curves)


---

## Events

2020-06-22: Added curation job to "Wishlist" (M.E.D.)
* Added list of datasets of interest

2020-06-22: Moved to "In-Progress" (M.E.D.)

2020-06-23: Assembled relevant datasets (D.J.)

2020-06-23: Generated mapping code (D.J.)

2020-06-23: Uploaded curation Excel files to repo (D.J.)

2020-06-23: Attempted upload of S1 to NanoMine QA (M.E.D.)
* Received "Success!" email (2:22pm)
* Successfully uploaded S2-S5
* Received error uploading S6 (2:25pm) (see Issue 1)
* Contacted D.J. to update template/re-run mapping code

2020-06-24: Updated code and re-uploaded filesets (D.J.)
* Also fixed column headers (need to REUPLOAD S1-S5)

2020-06-24: Created new dataset for re-upload (L391) (M.E.D.)
* Attempted upload of S1 (received "success" email 6:42am)
* Successfully uploaded S2-S9 (6:43-6:46am)
* Received error uploading S10 (6:46am) (see Issue 2)

2020-06-24: Contacted NM systems team regarding Issue 2 (M.E.D.)

2020-06-25: Reviewed error logs for failed upload (M.E.D.)
* Noticed issue related to "Frequency"
* Identified likely error in template
* Contacted D.J. to update mapping code


---

## Open Issues

### Issue 2
> Unfortunately, your conversion job xmlconv-wfYcpKSzbkvVaLcs95pEUy was not successful.
> job result code: 21
> error messages: [Conversion Error] Oops! The conversion cannot be finished! Please contact the administrator.

**Error:** For "Frequency sweep" DMA data, XML conversion fails when there is a value in the "Frequency" row

**Fix:** The constant temperature value (for S10, this value is 160 Celsius) should go in the Temperature row.

---

## Closed Issues

### Issue 1
 > Unfortunately, your conversion job xmlconv-k4eahXh4MGFA3dBbBHUzMu was not successful.
> job result code: 21
> error messages: [XML Schema Validation Error] Element 'value': 'twice its weight ratio' is not a valid value of the atomic type 'PositiveValueType'

**Error:** In the Processing section, "Additive - amount" features a text description, but the schema expects a positive numeric value

**Fix:** Leave this cell blank

---

## Sub-directory Contents

* `master_template.xlsx`
* `_notebook.Rmd`
* `/RawDataFromAuthors/`
* `/Images/`
* `/SUBMISSION/`
