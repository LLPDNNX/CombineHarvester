# Setting limits for LLP analysis

## Step 1: Produce histograms

* script ```driver.py``` defines what histograms to produce per category, systematic variation, lifetime, and llp/lsp mass pair
* script ```produceHist``` generates the batch submission file

## Step2: Produce datacards and run combine

* script ```produceDatacards.py``` produces a datacard lifetime and llp/lsp mass pair

## Step3: Collect results

* parse results into json files ```combineTool.py -M CollectLimits <folder>/ctau*/*AsymptoticLimits*.root --use-dirs -o limits.json```
* plot limits using ```plotLimit.py```


