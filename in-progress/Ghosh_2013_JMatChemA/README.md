CURATION JOB TRAVELER

# Ghosh_2013_JMatChemA

**Description:** Published article by Ghosh *et al.* on silica/PET nanocomposites.

---

**Traveler Created:** 2020-06-22

**Traveler Modified:** 2020-08-10

**Current Status:** *In-Progress*

---

## Bibliographic Info

* DOI: 10.1039/c3ta10381a

---

## Datasets of Interest

> Aerosil® R202 (SiAR), APS treated silica (SiAP) or APS-acetic anhydride (SiAc) treated silica
* samples were prepared as pellets, and also in bottle form (can ignore bottles for now because complex processing)
* Table 3: crystallization temperature, melting temperature, and glass transition temperature (pellet form)
* Fig 6: Storage modulus vs. Temperature

---

## Events

2020-06-22: Added curation job to "Wishlist" (M.E.D.)
* Added list of datasets of interest

2020-06-22: Moved to "In-Progress" (M.E.D.)

2020-07-31: Submission files uploaded as well as mapping code (D.J.)

2020-08-10: Attempted upload of S1 (M.E.D.)
* Received error message 9:37 AM (see Issue 1)

2020-08-10: Edited Mapping.py code to fix Issue 1 (M.E.D.)
* Changed filename output in lines 71 and 74
* Error running code (missing "G'(T).xlsx" template file for storage modulus data)
* Added this file, successfully ran code to re-generate sample files

2020-08-10: Re-attempt upload of S1 (M.E.D.)
* Received "success" email 10:06 AM

2020-08-10: Attempted upload of S2-S7 (M.E.D.)
* Received error message for S2 10:07 AM (see Issue 2)
* Contacted T.F. requesting error log for xmlconv-fjbHREHyEZHRdzavP6bzHu

---

## Open Issues

### Issue 2
>Unfortunately, your conversion job xmlconv-fjbHREHyEZHRdzavP6bzHu was not successful.
>job result code: 21
>error messages: [Conversion Error] Oops! The conversion cannot be finished! Please contact the administrator.

**Error:** 
**Fix:** 

---

## Closed Issues

### Issue 1
>Unfortunately, your conversion job xmlconv-qcYkCyT9w5j96REQuy69bW was not successful.
>job result code: 21
>error messages: [File Error] Missing file! Please include "S1/storage_modulus.xlsx" in your uploads.

**Error:** Filename filed in Excel template includes directory
**Fix:** Update Mapping.py with filename handling e.g. 'S1_storage_modulus.xlsx'

---

## Sub-directory Contents

* `master_template.xlsx`
* `_notebook.Rmd`
* `/RawDataFromAuthors/`
* `/Images/`
* `/SUBMISSION/`
