CURATION JOB TRAVELER

# Natarajan_2013_Macromolecules

**Description:** Published article by Natarajan *et al.* (NanoMine) on effect of interfacial energetics on dispersion and Tg.

---

**Traveler Created:** 2020-06-09

**Traveler Modified:** 2020-06-11

**Current Status:** *Completed*

---

## Bibliographic Info

* DOI: 10.1021/ma302281b

---

## Datasets of Interest

* Glass transition temperature
* Particle surface treatment information
* Microstructures photos

---

## Events

2020-06-09: Added curation job to "Wishlist" (M.E.D.)

2020-06-10: Added data of interest (M.E.D.)
* Issue 1 and Issue 2 require resolution before data can be uploaded to NanoMine

2020-06-10: Moved curation job to "In-Progress" (M.E.D.)

2020-06-11: Added master_template_DOI, Samples_DOI and Mapping.py (D.J.)

2020-06-11: Added Images subdirectory containing microstructure photos (D.J.)

2020-06-11: Searched Natarajan thesis for absolute Tg values (D.J., M.E.D.)
* Fig 2.11 shows example DSC curve indicating Tg of 109.56 deg C for neat PMMA
* Did not find raw data for average Tg
* No DSC curves provided for other polymers of interest (PS, P2VP, PEMA)
* Will assemble and use reference table of Tg values from the literature in order to infer experimental Tg from delta-Tg values

2020-06-11: Compiled and added reference table for Tg from literature (M.E.D.)
* PS: Tg = 100 C
* PMMA: Tg = 105 C
* P2VP: Tg = 100 C
* PEMA: Tg = 65 C
* Note: PMMA Tg differs from example DSC curve of Fig 2.11 of thesis, but will proceed with this literature value (105 C)

2020-06-11 : added SUBMISSION subdirectory containing templates of each sample (D.J.)

2020-06-11: Attempted upload of S1 to NanoMine QA (M.E.D.)
* Error returned related to datatype (see Issue 3)

2020-06-11: Updated master_template, re-ran Python code (D.J.)

2020-06-11: Re-attempt upload of S1 to QA (M.E.D.)
* received "success" email (1:27 PM)
* uploaded samples S2-S12 (1:28-1:31 PM)
* encountered error with S13 (see Issue 4)

2020-06-11: Updated code to fix Issue 4, re-ran Python code (D.J.)

2020-06-11: Re-attempt upload of S13 (M.E.D.)
* received "success" email (1:51 PM)
* uploaded S14-S20 successfully (1:52-1:55 PM)

2020-06-11: Moved job to "Completed" directory (M.E.D.)


---

## Open Issues

### Issue 1

> How are particle surface energy values stored in the schema? Surface treatment of particles is an integral component of this work to control dispersion of nanoparticles by tuning surface energy.




---

## Closed Issues

### Issue 2

> The author reported all values of glass transition temperature (Tg) as relative values (ΔTg), but did not provide the Tg of the reference control samples (neat polymers). Some additional inference is required in order to input these data in the schema.

**Solution:** Made a best-effort search of paper and thesis for absolute Tg values. Created a reference table of Tg values for the 4 polymers of interest, including reference. These Tg values were used to calculate Tg for the samples, based on the reported delta-Tg values from the article.

### Issue 3

>Unfortunately, your conversion job xmlconv-nGTWhPLa3VGFsjhf9u4b1G was not successful.
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'value': '60−80' is not a valid value of the atomic type 'xs:double', should be a number.

**Error:** The value in the Excel cell describing sample thickness is not of type double (the author reported a range of 60-80 to convey uncertainty in sample thickness measurement)
**Workaround:** Replace value with the average (70), and keep this issue open so that it may be addressed in future improvements to curation process

### Issue 4
>Unfortunately, your conversion job xmlconv-7Pw8hkyKhhSapExahhi1Nc was not successful.
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'Description': This element is not expected. Expected is ( File )

**Error:** Sample contains no image, and hence no filename. However, master template contains image description, etc. related to other samples in the dataset that do have images.

**Fix:** Modify code to print blank strings "" to these cells in the "6. Microstructure" sheet if there is no image associated with the sample

---

## Sub-directory Contents

* `/Images/` contains microstructure photos
* `/SUBMISSION/` contains templates for each sample
* `Mapping.py` mapping function from Samples table to sample Excel template files
* `master_template_ma302281b.xlsx`
* `Reference_Tg_values.xlsx` list of reference Tg values pulled from literature as a substitute for control Tg values
* `Samples_ma302281b.xlsx` list of samples and relevant attributes to be mapped to sample Excel template files
