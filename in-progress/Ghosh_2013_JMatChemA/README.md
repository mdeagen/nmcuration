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
* Received "success" email for S1 (10:06 AM)

2020-08-10: Attempted upload of S2-S7 (M.E.D.)
* Received error message for S2 (10:07 AM) (see Issue 2)
* Contacted T.F. requesting error log for xmlconv-fjbHREHyEZHRdzavP6bzHu

2020-08-10: Received error log from T.F. (M.E.D.)
* Identified possible issue with special characters that may have caused error in Issue 1:
>mixture was then heated to 250°C under anitrogen atmosphere for the esterication phase.
>temperature was raised to 280C in the polycondensationreactor under vacuum to form a high molecular weight polyester
* Replaced special characters  and  in master templates
* Re-ran Mapping.py to generate sample template files

2020-08-10: Re-attempt upload of S2-S7 (M.E.D.)
* Received same error message (2:16 PM)
* Observed same problem special characters in `S2_template.xlsx`
* Earlier, had removed special characters from `master_template_APS.xlsx` and `master_template_APS_aa.xlsx`, but NOT `master_template.xlsx`
* Updated `master_template.xlsx`
* Re-ran Mapping.py
* Confirmed special characters no longer appearing in `S2_template.xlsx`

2020-08-10: Re-attempt upload of S2-S7 (M.E.D.)
* Received "success" email for S2 (2:23 PM)
* Successfully uploaded S3-S7 (2:26 PM - 2:27 PM)

---

## Open Issues



---

## Closed Issues

### Issue 1
>Unfortunately, your conversion job xmlconv-qcYkCyT9w5j96REQuy69bW was not successful.
>job result code: 21
>error messages: [File Error] Missing file! Please include "S1/storage_modulus.xlsx" in your uploads.

**Error:** Filename filed in Excel template includes directory
**Fix:** Update Mapping.py with filename handling e.g. 'S1_storage_modulus.xlsx'

### Issue 2
>Unfortunately, your conversion job xmlconv-fjbHREHyEZHRdzavP6bzHu was not successful.
>job result code: 21
>error messages: [Conversion Error] Oops! The conversion cannot be finished! Please contact the administrator.

**Error:** Related to "lxml.etree.XMLSyntaxError: PCDATA invalid Char value 14, line 1, column 2862"
**Fix:** Removed problematic special characters from Synthesis and Processing descriptions ( and )

---

## Sub-directory Contents

* `master_template.xlsx`
* `_notebook.Rmd`
* `/RawDataFromAuthors/`
* `/Images/`
* `/SUBMISSION/`
