CURATION JOB TRAVELER

# Ning_2019

**Description:** Published article by Ning *et al.* for the Macromolecules **Virtual Issue**

---

**Traveler Created:** 2020-06-05

**Traveler Modified:** 2020-06-08

**Current Status:** *Completed*

---

## Bibliographic Info

* DOI: 10.1021/acsmacrolett.9b00619
* SI: https://pubs.acs.org/doi/suppl/10.1021/acsmacrolett.9b00619/suppl_file/mz9b00619_si_001.pdf

---

## Datasets of Interest

* Table 1: Sample names with experimental factors (Matrix MW, graft density, NP Loading) as well as response variables melting temp (Tm) and degree of crystallinity (Xc)
* Dielectric spectra (matrix MW = 152k; NP loading = 0,0.10; crystallization process = "quenched","iso 128C")
* Dielectric spectra (matrix MW = 4k; NP loading = 0,0.10; crystallization process = "quenched","iso 105C")
* DMA results (matrix MW = 152k; NP loading = 0,0.10; crystallization process = "quenched","iso 128C")
* DSC results (matrix MX = 152k; NP loading = 0.10; crystallization process = "iso 125C","iso 128C","iso 129.5C")
* SAXS results (matrix MW = 152k; NP loading = 0; crystallization process = "quenched","iso 128C","iso 129.5C","iso 130C")
* SAXS results (matrix MW = 152k; NP loading = 0.10; crystallization process = "quenched","iso 128C","iso 129.5C")
* SAXS results (matrix MW = 4k; NP loading = 0,0.10; crystallization process = "quenched","iso 105C")
* TGA results (matrix MW = 4k,152k)

---

## Events

2020-06-02: (Virtually) added publication, curation job to "Wishlist" (M.E.D.)

2020-06-05: Added datasets of interest (M.E.D.)

2020-06-05: Added job to "In-Progress" (M.E.D.)

2020-06-08: Updated R code (M.E.D.)
* updates for R 4.0 compatibility (NA handling, tibble indices, etc)
* changed output datafiles from `.csv` to `.xlsx`

2020-06-08: Re-generated filesets for all samples (M.E.D.)

2020-06-08: Attempted upload of S1 fileset to NanoMine QA (M.E.D.)
* Not successful (contact administrator error)
* May be issue with R code outputting blank supplementary datafiles (R 4.0 issue with is.null checking)

2020-06-08: Re-attempted upload of S1 fileset to QA (M.E.D.)
* Not successful (files not found error)
* Requires update to R code similar to previous fix (where filenames are being added to Excel template)

2020-06-08: Re-attempted upload of S1 fileset to QA (M.E.D.)
* Received "successful" auto-generated email (5:14pm)

2020-06-08: Uploaded remaining filesets S2-S14 (M.E.D.)
* Files with supplementary images took long time to upload, without indicator of time remaining (S4 fileset, 191MB, took 9 min; S10 fileset, 43.5MB, took 2 min)
* Error with S13, S14 (see Issue 3)
* Confirmed issue with B.H., updated R code and re-ran for those samples

2020-06-08: Successfully uploaded S13, S14 to QA (M.E.D.)

2020-06-08: Moved job to "Completed" (M.E.D.)



---

## Open Issues



---

## Closed Issues

### Issue 1
>Unfortunately, your conversion job xmlconv-r2P2v6Ci5FdCavNsno8Amf was not successful.
>job result code: 21
>error messages: [Conversion Error] Oops! The conversion cannot be finished! Please contact the administrator.

**Error:** Caused by blank supplementary files? 

**Fix:** Update to R code (changed indices in is.null() check from `[[j]][i]` to `[[j]][[i]]`)

### Issue 2
>job result code: 21
>error messages: [File Error] Missing file! Please include "S1_DSC_data.xlsx" in your uploads. [File Error] Missing file! Please include "S1_TGA_data.xlsx" in your uploads. [File Error] Missing file! Please include "S1_DMA_storage_modulus.xlsx" in your uploads. [File Error] Missing file! Please include "S1_DMA_loss_modulus.xlsx" in your uploads. [File Error] Missing file! Please include "S1_DMA_tan_delta.xlsx" in your uploads.

**Error:** These filenames should not be written to the template. 

**Fix:** Update to R code (if filename should not be in template, change filename to "")

### Issue 3
>job result code: 21
>error messages: [XML Schema Validation Error] Element 'unit': This element is not expected. Expected is one of ( description, value )

**Error:** These samples do not have a value for Melting Temperature, however master template includes "Celsius" as unit (even if value is blank)

**Fix:** Add lines in R code to print "" into Unit cell for samples where `melting_temp` is NA


---

## Sub-directory Contents

* `master_template_2020_Ning.xlsx`
* `Ning_2019_notebook.Rmd`
* `table1.xlsx`
* `Process_Ning_PNC_4k.xlsx`
* `Process_Ning_PNC_152k.xlsx`
* `Process_Ning_SurfaceChemical.xlsx`
* `/RawDataFromAuthors/`
* `/Images/`
* `/SUBMISSION/`
