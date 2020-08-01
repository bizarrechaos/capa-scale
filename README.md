# capa-scale
Fireeye [Capa](https://github.com/fireeye/capa) scale for Countercept [Snake](https://github.com/countercept/snake)

## Disclaimer

This is a work in progress.  
Your mileage may vary.  
Please feel free to make a pull request with any additions/fixes you may have.  

## Installation

This scale can be installed in two way, pip or by cloning the respository and pointing Snake to it.  
Once installed Snake and the Celery workers must be restarted.  
> Note: Any missing dependencies will be reported in Snake's log!  

### Pip Based

A scale can be installed using pip as follows:

```bash
# 1. Install the scale with pip
pip install git+https://github.com/bizarrechaos/capa-scale

# 2. Install system dependencies
# If any, these will be reported in the Snake log, or usually listed in the `check` functions within components
```

### Clone Based

All the scales from a repository can easily be added to Snake, just by cloning and pointing.

```bash
# 1. Clone the repository to the desired location
git clone https://github.com/bizarrechaos/capa-scale.git <SCALE_DIR>

# 2. Add directory to snake.conf
[snip]
snake_scale_dirs: [ '<SCALE_DIR>' ]
[snip]

# 3. Install python requirements
# If any, either look through the setup.py files or look at the Snake log.

# 4. Install system dependencies
# If any, these will be reported in the Snake log, or usually listed in the `check` functions within components
```
