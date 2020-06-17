# Dielectric Breakdown Strength re-curation

## Description
Dielectric Breakdown Strength (typically V/m or kV/mm) should be stored as `nm:DielectricBreakdownStrength` in the NanoMine Knowledge Graph. Due to schema structure, the value for //DielectricBreakdownStrength is nested inside a \<Profile\> element in the XML. This structure differs from the convention for other properties in NanoMine.

This sub-directory contains a file with raw data from datasets already in NanoMine. These data should ultimately reside as DielectricBreakdownStrength values in the KG.

These data are linked to Weibull plots, and the modeling of Weibull information should also be addressed. However, the Weibull plot data should also coincide with a new curation tool for digitally extracting raw data from Weibull plots.