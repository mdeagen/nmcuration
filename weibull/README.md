# Weibull Plot Extraction Guide 

This documentation provides step-by-step instructions on extracting data from Weibull plots using the [WebPlotDigitizer](https://apps.automeris.io/wpd/). 


## Introduction

Dielectric breakdown tests measure the cumulative probability of failure as a function of electric field. Insulator materials typically follow a Weibull distribution, and Weibull plots are commonly presented in research articles in the Results section.

The x-axis in a Weibull plot typically follows a logarithmic scale. The y-axis is scaled by ln(-ln(1-p)), where p is the cumulative probability of failure.

While the WebPlotDigitizer allows for logarithmic axis calibration, the tool does not include Weibull axis calibration. Therefore, we must extract the data as a **linear** scale, then convert to probability ourselves.


## Linear Calibration of Weibull y-axis

Typically, the author will label the y-axis with the probability of failure. In the end, these probabilities are the numeric values we want to extract as a function of the independent variable (electric field).

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


In the below example, where Y-axis calibration labels are 1 and 99, you will type -4.6 and 1.527 respectively, and keep as a *linear scale*.

![Screenshot of Weibull axis calibration](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/calibration.PNG)


## Extraction of Data

Once the axes have been calibrated, use auto-extract or manual extraction to capture the x-y data. **Copy these data to the clipboard** and paste into the X column of the `Weibull_converter.xlsx` spreadsheet ([link to download](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/Weibull_converter.xlsx)).

![Screenshot of extracted data from WebPlotDigitizer](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/view-data.PNG)

While these pasted rows are highlighted in Excel, use Data > Text to columns > Comma delimited to convert the .csv data into two columns, X and Y. The converted values will appear in the columns to the right.

![Screenshot of converted Weibull data](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/conversion.PNG)

**After confirming that the x-axis units are correct**, copy the converted data into its own separate file (including column headers) and name the file with the corresponding sample ID (e.g., `S1_weibull.xlsx`).


## Entering Weibull Data into Schema Excel Template

In sheet "`5.3 Properties-Electrical`" of the Excel template, ensure that the correct filename is placed in cell `C27`. When the mapping code creates a sub-directory for a given sample, ensure that a copy of the file (e.g., `S1_weibull.xlsx`) is included in that sub-directory.

![Screenshot of filled-out Excel template](https://github.com/mdeagen/nmcuration/blob/master/weibull/www/template.PNG)


## Uploading Curated Data into NanoMine

When curating a sample fileset into NanoMine, include the Weibull data as an attachment.




