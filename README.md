# GMID-Designer

A tool intended for determining sizings for intial designs for analog SSI, MSI and even LSI and VLSI utilizing $g_m/I_D$ design methodology.

## What is $g_m/I_D$ Design Methodology?

$g_m/I_D$ Design Methodology is a technique often used by designers to get an idea of how to size transistors for thier applications.

## Installation

To install this you would need to do... TO DO: How do we install this?

## Getting Started

### Formating your Data for gmidDesigner

Before one can fully utilize the power of this solver, we need to make sure that the data is listed as follows:

```text
vov gmoverid gmoverid jd ... gmoverid variable_you_want_to_capture
```

### Loading Data

Before one can fully utilize power of this solver, we need to give it technology data. Provided in the source code within the `sample_data` directory is the technology data for the Google/Sky130nm process. To load this data, you can execute:

```text
load $PATH_TO_NMOS_DATA $PATH_TO_PMOS_DATA
```

**NOTE**: The SKY130 PDK displays some non-ideal/realistic $g_m/I_D$ plots for the PMOS process. Keep this in mind when designing/using this tool.

### Plotting/Visualizing Data

Often you might want to get an idea of what the solver is working with. You can view plots using the following command

```text
plot vov gmoverid NMOS
```

Suppose if you wanted to view this plot for a PMOS instead. You can execute the following command:

```text
plot vov gmoverid PMOS
```

Suppose if you wanted create a plot for all variables. You can execute the following command:

```text
plot all PMOS
```

Suppose you wanted to save this plot. You can execute the following command:

```text
plot vov gmoverid PMOS >> $PATH_TO_SAVE
```

If a filename ending in a valid extension, it will save as a `pdf` under the following naming scheme `Yydata.Xxdata.pdf`:

```text
plot vov gmoverid PMOS >> ./example_path/
```

This would output:

```text
Plot saved as ./example_path/Ygmoverid.Xvov.pdf
```

Suppose instead you would like to know all the parameters associated with a specific gmid value. You can do this with the following command:

```text
NMOS @ gmid 10
```

This should output the following:

```text
jd 22.5 gmovergds 15.5 ...
```

Suppose instead you like to know at what $g_m/I_D$, produces a certain $J_D$. You can execute:

```text
NMOS @ jd 22.5
```

This should output the following:

```text
vov 0.1 gmoverid 10 gmovergds 15 ...
```

You can pipe the output of any function to a file if you would like with `>>` operator:

```text
NMOS @ gmid 10 >> $PATH_TO_FILE
```

### Sizing from Data

Suppose you would like to determine the size of the transistor. As mentioned before mentioned, you would need a drain-source current specification or to determine the width. Using this current, we can divide it by the current density to determine the appropiate sizing:
$$
W=\frac{I_{DS}}{J_{DS}}
$$
To do this uwing gmidDesigner, you can execute the following:

```text
size NMOS @ gmid 10 id 50u
```

This should output the following:

```text
W = 2.2222u
```

Suppose you would like this width in terms of a unit width $U$, where $U=2.2\ \mu\text{m}$:

```text
size NMOS @ gmid 10 id 100u unit U = 2.2u
```

This should output the following:

```text
nf = 2 W = 2U
```

Suppose you would like this width in terms of a unit width $U$, where $U=2.2\ \mu\text{m}$:

```text
U = 2.2u # Create a variable for the unit width
size NMOS @ gmid 10 id 75u unit U
```

This should output the following:

```text
nf = 3 W = 2.6666U
```
