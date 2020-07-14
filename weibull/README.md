# Weibull Plot Extraction Guide 

This documentation provides step-by-step instructions on extracting data from Weibull plots using the [WebPlotDigitizer](https://apps.automeris.io/wpd/). 


## Introduction

Dielectric breakdown tests measure the cumulative probability of failure as a function of electric field. Insulator materials tend to break down under electrical stress in a statistical manner following a Weibull distribution. As a result, Weibull plots are commonly used in research articles to present experimental data in the Results section.

The x-axis in a Weibull plot (usually) follows a logarithmic scale. The y-axis is scaled by *ln(-ln(1-p))*, where *p* is the cumulative probability of failure.

While the WebPlotDigitizer allows for logarithmic axis calibration, the tool **does not** include Weibull axis calibration. Therefore, we must extract the data as a **linear** scale, then convert to probability ourselves.


## Linear Calibration of Weibull y-axis

In most Weibull plots, the y-axis label is the probability of failure. These values of the dependent variable (cumulative probability) are the numeric values we want to extract as a function of the independent variable (Electric field, typically in units of kV/mm). [**Note:** 1 kV/mm = 1 V/μm = MV/m]

Here is a conversion table between y-axis labels (probabilities) and the linearized value. When calibrating the axis, type the value from the right hand column corresponding to the appropriate label. 

| Weibull  y-axis label | ln(-ln(1-p)) |
|-------|--------------|
| 99.9 | 1.933 |
| 99 | 1.527 |
| 90 | 0.834 |
| 80 | 0.476 |
| 70 | 0.186 |
| 60 | -0.087 |
| 50 | -0.367 |
| 40 | -0.672 |
| 30 | -1.031 |
| 20 | -1.5 |
| 10 | -2.25 |
| 5 | -2.97 |
| 1 | -4.6 |


In the below example, where y-axis calibration labels are 1 and 99, you would type -4.6 and 1.527 respectively, and keep as a *linear scale*.

![Screenshot of Weibull axis calibration](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/calibration.PNG)


## Extraction of Data

Once the axes have been calibrated, use auto-extract or manual extraction to capture the x-y data. **Copy these data to the clipboard**. 

![Screenshot of extracted data from WebPlotDigitizer](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/view-data.PNG)

Paste these data into the X column of the `Weibull_converter.xlsx` Excel spreadsheet ([link to download](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/Weibull_converter.xlsx)). While the pasted rows are highlighted, use *Data* > *Text to columns* > *Comma delimited* to convert the .csv data into two columns, X and Y. The converted values will appear in the columns to the right, as in the below example.

![Screenshot of converted Weibull data](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/conversion.PNG)

Before proceeding, perform a visual spot-check that the extracted datapoints correspond to what is visually presented in the plot. For example, the above example **fails** because the y-axis appears to have some scaling other than ln(-ln(1-p)). **See "Alternate y-axis Scaling" section below.**

If the extracted data pass visual inspection, **confirm that the x-axis units are correct** and copy the converted data into its own separate file (including column headers) and name the file with the corresponding sample ID (e.g., `S1_weibull.xlsx`).


## Entering Weibull Data into Schema Excel Template

In sheet "`5.3 Properties-Electrical`" of the Excel template, ensure that the correct filename is placed in cell `C27`. When the mapping code creates a sub-directory for a given sample, ensure that a copy of the file (e.g., `S1_weibull.xlsx`) is included in that sub-directory.

![Screenshot of filled-out Excel template](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/template.PNG)


## Uploading Curated Data into NanoMine

When curating a sample fileset into NanoMine, include the Weibull data as an attachment.


# Alternate y-axis Scaling

Some plotting software may distort the y-axis of output plots with an additional power law term, such as ln(-ln(1-p^n)), where n is a positive number. Such scaling is found in Weibull plots by Grabowski *et al.*, where n = 0.08.

Below is a table with the linearized y-axis scale values for this alternate scaling.

| Weibull  y-axis label | ln(-ln(1-p^0.08)) |
|---|---|
| 99 | 1.964 |
| 90 | 1.565 |
| 50 | 1.072 |
| 10 | 0.578 |
| 1 | 0.163 |

The linearized scale would use values from this table instead, such as 0.163 and 1.964 shown below.

![Screenshot of Weibull axis calibration](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/altscale1_calibration.PNG)

The acquired data using this alternate scale calibration can then be copied to the clipboard.

![Screenshot of extracted data from WebPlotDigitizer](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/altscale1_view-data.PNG)

Because we added a power term (n), converting back to probabilities will need to account for this term:

>p = (1 - e^(-e^y))^(1/n)).

An Excel file for converting Grabowski *et al.* where n = 0.08 has been added to this repo (`Weibull_converter_altscale1.xlsx`, download [here](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/Weibull_converter_altscale1.xlsx)).

![Screenshot of converted Weibull data](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/altscale1_conversion.PNG)

Upon inspection, these data match those values reported on the plot much more closely and may be curated into NanoMine.