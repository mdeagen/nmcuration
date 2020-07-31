CURATION JOB TRAVELER

# Koerner_2005_Polymer

**Description:** Published article by Koerner *et al.* (AFRL) on electrically conductive carbon nanotube nanocomposites.

---

**Traveler Created:** 2020-06-05

**Traveler Modified:** 2020-07-31

**Current Status:** *In-Progress*

---

## Bibliographic Info

* DOI: 10.1016/j.polymer.2005.02.025

---

## Datasets of Interest

* Fig 2: DC conductivity vs. volume fraction
* Fig 3a,b: Stress-strain (note samples not labeled in 3a)
* Fig 4a-b,d: Mechanical characterization (note b-d have dual y-axes) vs mass/volume fraction (reported as %)
* Fig 5: Melting enthalpy
* Fig 11: Degree of crystallinity vs. strain (plus elongation at yield)

---

## Events

2020-06-05: Added curation job to "Wishlist" (M.E.D.)
* Added list of datasets of interest

2020-06-08: Added datasets from AFRL collaborators (M.E.D.)
* Not all of these datasets will be used, but "Datasets of Interest" should be among these
* `.opj` is only openable with Origin (freely available [Origin Viewer](https://www.originlab.com/viewer/) can be used to read these)
* Should convert relevant tabular datasets to `.csv` for processing

2020-06-08: Added master excel file for data curation (H.D.)
* Currently an initial draft covering the overall information
* This excel file can be used as a starting point for each of the following samples
* `Koerner_2005_Polymer_Master.xlsx`

2020-06-12: Added Tidy Table and updated master excel file (H.D.)
* The initial draft of the Tidy Table is included with all inflormation in one location
* The master excel file has been updated (`Koerner_2005_Polymer_Master.xlsx`)
* `Koerner_2005_Polymer_Tidy_Table.xlsx`

2020-06-15: Meeting to discuss curation items (M.E.D., H.D.)
* Schema does not currently have a term for "stress/elongation at onset of strain hardening" (in this paper, this term is distinct from "stress at yield")
* For now, ignore strain hardening term, and only include stress and strain at yield for Figs 4, 11
* Keep these data in the Tidy Table in case schema is expanded
* Updated Datasets of Interest for Fig 4, 11

2020-06-15: Moved curation job to "In-Progress" (M.E.D.)

2020-07-17: Updated Tidy Table and added "Additional Data" (H.D.)
* Added new folder with Additional Data
* Updated Tidy Table with additional data file names included

2020-07-20: Made updates to tidy table (M.E.D.)
* Fig 3 data - need to add weight% or vol%
* Fig 5 - each point should be its own sample (samples at diff temps? 48 and 135)
* Fig 11 - x-axis is elongation

2020-07-31: Created Issue 1 related to Fig 3 (M.E.D.)
* Attempted to find wt% labels for datasets among raw data
* Closed Issue 1

2020-07-31: Updated Master Template (H.D.)
* Included finishing touches on Synthesis and Processing
* Updated Filler information

2020-07-31: Finished python code (H.D.)
* Uploaded the working python code
* Ran without error and created SUBMISSION folder

2020-07-31: Added SUBMISSION (H.D.)
* Uploaded SUBMISSION folder with sample subfolders
* Should be finalized sample submissions

2020-07-31: Made edits to master template (M.E.D.)
* thermoplastic --> elastomer (paper lists as "thermoplastic elastomer" so there is no right answer; chose elastomer because thermoplastic is used here as a modifier of elastomer type)
* copolymer --> homopolymer

2020-07-31: Re-ran Python code (M.E.D.)
* stress-strain files for S12-S16 not copied from "/Additional Data/Stress-Elongation/" Directory?

---

## Open Issues



---

## Closed Issues

### Issue 1

> Fig 3 stress-strain curves are not labeled with the respective samples. Raw data include "1%", "1%cb", and "1%repeat" data. "1%" and "1%repeat" show lower stress-strain curve than neat matrix, however "1%cb" supports the trend of increasing stress-strain with increasing volume fraction.

**Workaround:** Curate Fig 3 data as presented, and assume labels of (0 vol%, 0.57 vol%, 2.9 vol%, 5.9 vol%, 10.2 vol%) apply to the curves in increasing order as implied by the caption.


---

## Sub-directory Contents

* `master_template.xlsx`
* `_notebook.Rmd`
* `/RawDataFromAuthors/`
* `/SUBMISSION/`
