## Weibull Plot Extractor Tool

**Status:** *Wishlist*

### Objective

Create a tool that curators can use to easily extract the underlying raw data from images or screenshots of Weibull plots. For more information about Weibull plots, visit [this link](https://www.itl.nist.gov/div898/handbook/eda/section3/weibplot.htm). The tool would accomplish what the [Web Plot Digitizer](https://apps.automeris.io/wpd/) accomplishes for more standard plot types.

### Needs

User should be able to:

* Upload an image of a plot from any standard format (.png, .jpg, .bmp)
* Calibrate the x- and y-axis scales
* Extract (manually or in automated fashion) individual series of data
* Define a name for each data series (for keeping track of multiple series)
* Download the tabular data in a tidy format (.csv)

### Axis Scales

Weibull plots are scaled on the vertical axis such that a Weibull distribution becomes linear. The vertical scale is `ln(-ln(1-p))`. When the user selects endpoints of the scale (such as 0.5 and 99.9), the pixel interpolation should scale appropriately.

The horizontal axis is typically on a logarithmic scale, but may also be scaled linearly (in which case the distribution follows a curve).

### Links and Resources

* [Characteristics of Weibull distribution](https://www.weibull.com/hotwire/issue14/relbasics14.htm)
* [Weibull Distribution on ReliaWiki](http://reliawiki.org/index.php/The_Weibull_Distribution)
* [NIST Engr Statistics Handbook](https://www.itl.nist.gov/div898/handbook/eda/section3/weibplot.htm)
