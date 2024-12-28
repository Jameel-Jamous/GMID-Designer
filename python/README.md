# Commands
GMIDDesigner has a small and simple interface. The execution structure is typical UNIX style commands such as:

```text
gmid [OPTIONS] COMMAND [ARGS]...
```

## Command List

### Data Management Related Commands

- *link* [--path=PATH_TO_DATA] [--nmos --pmos]
- *unlink* [--nmos --pmos]
- *view* [--path] [--header]

### Interpolation Related Commands

- *set* [--gmid] [--header1] [--header2] [--header3] ... [--headerN]
- *view* [--header1] [--header2] [--header3] ... [--headerN] [--all] [--annotated]

### Plotting Related Commands

- *plot* [--header1] [--header2] [--header3] ... [--headerN] [--all] [--s/seperate]
- *plotvs* [--axis-y=<Ydata\>] [--axis-x=<Xdata\>]

### Designing Related Commands

- *set* [--gmid] [--header1] [--header2] [--header3] ... [--headerN]

TODO: Think of some commands to call gmid to determine the sizing of a transistor
based on the `set` parameter. For example if `gmid` is set to `10`, we can do a command that determines the width needed for a certain $I_D$. That is, $W=I_D/J_D$ (output).

NOTE: You need to know $I_D$ at all times to relate back to $W$.
Thus, user must have a data column that contains `jd`. So this implies, a `VALID_FILE` is now one that contains `vov,gmid,jd`

NOTE: Maybe execution like `gmid size --id=100u --unit=2.2u` with the output
looks like:

```text
For gmid = 10 S/A and id = 100 uA:

Exact(um):      W = 13.567, 
Whole(um):      W = 13 +/- 1, 
Unit (2.2um):   W = 7 * unit

Other Metrics:

vov = 0.784 V, jd = 19.321 A/m, gmovergds = 18.800 S/S, 
cdsovercgs = 1.352 F/F
```

```text
For jd = 100 A/m and id = 100 uA:

Exact(um):      W = 1, 
Whole(um):      W = 1 +/- 0, 
Unit (um):      W = 1 * unit

Other Metrics:

vov = 0.984 V, gmid = 10.231 A/m, gmovergds = 17.800 S/S, 
cdsovercgs = 2.352 F/F
```

NOTE: If a variable other than `gmid` or `jd` is `set`, then you get a sitution
with multiple solutions. How do we fix this? Do we want to throw errors? Do we
want to optimize? Converge to nearest solution (newton-raphlson)?

TODO: Add another commond that will `match` the given params from `nmos` to `pmos`. Think of second stage of project

## Examples

The following examples assumes if you have data with the following headers:

```text
vov,gmid,jd,gmovergds,cdsovercgs
```

### Interpolation Examples

#### Setting `gmid`

Suppose you want to determine what $J_D$ is at a $g_m/I_D=10\;\text{S/A}$.
To do this, one must first set the interpolation value to `10`:

```text
gmid set 10 # which is equivalent to: gmid set --gmid=10
```

#### Viewing/Interpolating Data

Now one can view the interpolation results with the following command:

```text
gmid view --jd
```

The **output** should look like:

```text
For gmid = 10 S/A:

jd = 14.667 A/m
```

After setting `gmid`, we can view other data at this gmid as follows:

```text
gmid view --jd --gmovergds
```

The **output** should look like:

```text
For gmid = 10 S/A:

jd = 14.667 A/m, gmovergds = 17.879 S/S
```

To view **all** data, we can use the following command:

```text
gmid view --all
```

The **output** should look like:

```text
For gmid = 10 S/A:

vov = 0.987 V, jd = 14.667 A/m, gmovergds = 17.879 S/S,
cdsovercgs = 7.805 F/F
```

#### Setting & Viewing Other Data

Suppose now instead of determining the parameters amongst a set $g_m/I_D$,
    we would like to determine what $g_m/I_D$ is needed for a $J_D=10\;\text{A/m}$.
To do this we can set `jd` to `10` instead by using the following command:

```text
gmid set --jd=10
```

The same commands can be ran to see the results of the interpolation. That is:

```text
gmid view --all
```

The **output** should look like:

```text
For jd = 10 A/m:

vov = 0.765 V, gmid = 8.774 S/A, gmovergds = 14.345 S/S,
cdsovercgs = 5.678 F/F
```

#### Viewing with Plot Annotations

You can set the output to give you an annotated plot showing the interpolated     value on the plot.
To do this you can execute the following command:

```text
gmid set 10 
gmid view --jd --annotated
```

The **output** should look like:

```text
TODO: PUT THE PLOTS HERE AND WHAT YOU WOULD SEE ON CLI
```

You can also view annotated plots for multiple data as follows:

```text
gmid view --all --annotated
```

The **output** should look like:

```text
TODO: PUT THE PLOTS HERE AND WHAT YOU WOULD SEE ON CLI
```

### Plotting Examples

#### Plotting against `gmid`

To generate plots against gmid 