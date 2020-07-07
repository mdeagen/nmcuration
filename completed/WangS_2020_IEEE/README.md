CURATION JOB TRAVELER

# WangS_2020_IEEE

**Description:** Published article by S. Wang *et al.* from IEEE nanodielectrics issue

---

**Traveler Created:** 2020-06-16

**Traveler Modified:** 2020-07-07

**Current Status:** *Completed*

---

## Bibliographic Info

* DOI: 10.1109/TDEI.2019.008572

---

## Datasets of Interest

* Fig 4: DC breakdown strength as a function of Temperature
* Fig 7: Dynamic thermomechanical analysis (DMTA) data; each "curve" is a single sample
* Fig 9: DC breakdown strength vs. Elastic modulus; each "point" can be considered a sample, ignore fitted curves


---

## Events

2020-06-16: Added curation job to "Wishlist" (M.E.D.)
* Added datasets of interest
* Added Issue 1 related to schema

2020-06-23: Included Tidy Table Excel sheet to master repo (H.D.)
* `WangS_2020_IEEE_Tidy_Table.xlsx`
* Currently includes initial data tables for Figures 4,7, and 9

2020-07-02: Finalized Master Template (H.D.)
* `WangS_2020_IEEE_Master.xlsx`
* Updated the processing and filler information
* Finalized and prepared for the code

2020-07-06: Finalized code and created submissions folder (H.D.)
* Submissions folder created will all 24 samples

2020-07-07: Control sample submissions corrected (H.D.)
* Erased filler information in control sample submissions
* Control samples should have no filler information

2020-07-07: Attempt upload to NanoMine QA (M.E.D.)
* Received error message for S1 (see Issue 2)

2020-07-07: Re-attempt upload of S1 (M.E.D.)
* Received error message related to particle surface treatment (see Issue 3)

2020-07-07: Re-attempt upload of S1 (M.E.D.)
* Received "Success!" message (10:26 AM)

2020-07-07: Master template updated and code re-run (H.D.)
* Updated master template to prevent error messages in upload
* Re-ran the code to update submissions

2020-07-07: Moved curation job to completed (H.D.)
* All uploads were successful and the curation job is now in the completed folder

---

## Open Issues



---

## Closed Issues

### Issue 1

> How to represent material state (e.g. Temperature)... and at what point does this become a different "sample"?

**Workaround:** Included temperature as final "Heating" step of Processing

### Issue 2

>Unfortunately, your conversion job xmlconv-7zYZYFpxjAFZvzRc4bfC3i was not successful.
>job result code: 21
>error messages: exception occurred during mass fraction-volume fraction conversion exception: Traceback (most recent call last): File "/apps/nanomine/src/jobs/XMLCONV/code_src/conversion.py", line 292, in conversion mvc.run() File "/apps/nanomine/src/jobs/XMLCONV/code_src/mfvf.py", line 316, in run self.computeFiller() File "/apps/nanomine/src/jobs/XMLCONV/code_src/mfvf.py", line 77, in computeFiller raise LookupError('[Filler Error] FillerComposition is missing.') LookupError: [Filler Error] FillerComposition is missing.

**Error:** Filler information included for control sample (where there is no filler composition)

**Fix:** Manually removed filler information.

### Issue 3
>Unfortunately, your conversion job xmlconv-a1LsXomRRiFXcHr4HyuZj2 was not successful.
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'ParticleSurfaceTreatment': This element is not expected. Expected is ( ChemicalName )

**Error:** Surface chemical processing info existed, but no filler in control sample

**Fix:** Manually removed surface chemical processing for S1



---

## Sub-directory Contents

* 
