# GMID-Designer

A tool intended for determining sizings for intial designs for analog SSI utilizing $g_m/I_D$ design methodology.

## What is $g_m/I_D$ Design Methodology?

$g_m/I_D$ Design Methodology is a technique often used by designers to get an idea of how to size transistors for thier applications.

TO DO: Elaborate more and cater to the repo

If you would like to know more the following is a pretty good paper to read: [A Basic Introduction to the gm-id Based Design Methodology](https://picture.iczhiku.com/resource/eetop/SHITwppaOwepYMBX.pdf) 

## Installation

TO DO: Provide installation instructions

```text
export GMID_INSTALL_PATH=<path-to-python>
export GMID_DATA_PATH=<path-to-your-data>/example_data.csv
export GMID_CONFIG_PATH=<path-to-your-config>/example_config.json
export GMID_OUTPUT_PATH=<path-to-place-your-output>
export GMID_PATHS=$GMID_INSTALL_PATH:$GMID_DATA_PATH:$GMID_CONFIG_PATH:$GMID_OUTPUT_PATH
```

After paths are established, you can verify that the tool is using them by running the following commands:
```text
gmid view
```

## Getting Started

### Preparing your Data for GMID-Designer

Before one can fully utilize the tool, we need to make sure that the header line of your data formatted in a certain way:

```text
vov gmoverid jd ... cdsovercgs variable_you_want_to_capture
```

Remember you need to set the `GMID_DATA_PATH` to point to your data. Also, note that the way the headers are formatted will be the way they are formatted on the plots.     

### Setting the Design Header

By default, the design header is `gmid`. You can establish the value to be visualized by running the following command:

```text
gmid set 10
```

You can also set the design header to be any other header provided in your data. Use the following as an example:

```text
gmid set 10 -h vov
gmid set 10 --head vov
```

### Interpolation

Often you might just want an idea of what the values are at that $g_m/I_D$ values. You can do so running the following command
after you have already `set` the header:

```text
gmid interp vov
```

The output should look like:

```text
For 'gmid' = 10.0:
  'vov' = 1.232
```

Note that you cannot interpolate the set value with the set header:

```text
gmid interp cdsovercgs   # Valid Syntax
gmid interp gmid         # Invalid Syntax!
```

TO DO: Explain batch mode

### Plotting

To view a plot of the set header with respect to another header you can execute the following command:

```text
gmid plot vov
```

If you are using the default configuration for the tool, your output should look like:

![Single Plot Data](./imgs/sample_plot1.png)

You can also view a plot that is with respect to all of the other headers by using `all`., running the following command should produce the following figure.
`all` is an internal header that is only used by the tool and should not be set in header line of your data. 

```text
gmid plot all
```

#### Plot Annotations

You can also add annotations to your plots by doing the following:
```text
gmid plot all --annotated
```
If you are using the default configuration for the tool, your output should look like:

![Single plot annotated](./imgs/sample_plot2.png)

#### Versus Plotting

TO DO: Talk about `VSPLOT` command.

