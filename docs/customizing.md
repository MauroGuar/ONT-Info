# Customizing

## Remember that all these changes take effect after restarting the service, there is no such thing as hot-reloads

## UI

### Items to show in result

You can change which items to show without inside the [results_app.js](/app/static/js/results_app.js) file, the variable named itemsToShow, which is an array, should contain all the data keys you want to show in a filtered manner from the retrieved json, the data can or cannot be on the json, the data keys should be all in lower case letters, since when the data is processed, all letters are converted to small caps.

### IP selection

You can change the IPs selection to choose from when searching inside the [index_app.js](/app/static/js/index_app.js) file, the constant named oltIpOptions, which is an array, should contain all the OLT ips compatible with this software.

## data_processing

### Debug mode

You can change the debug mode to true if you dont want the app to use real connections inside the [main.py](/app/main.py) file, changing the boolean variable debug_mode using instead a string as the value retrieved, this is useful in a scenario where you want to have something functional as a demonstration, this also test the processing part of the code, like the regex and whatnot.

### commands to olt 

To change the commands given to the olt, you can do so by changing the get_ont_info_prompt function or the get_ont_optical_info_prompt function inside the [ont_info.py](/app/data_processing/ssh_prompt_handler/ont_prompt.py) file

### regex

You can change the regex as you wish inside the [prompt_analysis.py](/app/data_processing/ssh_prompt_handler/prompt_analysis.py) file, constant REGEX_PATTERN.

