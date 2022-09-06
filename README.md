# ebook-complexity-score

# installation

```
git clone https://github.com/jeffgreenca/ebook-complexity-score.git
pip install -r requirements.txt
```

# usage
1. make sure your books are in epub format and end with .epub
1. folder structure must be as shown:
```
group1\
  book-folder-a\
    book-a.epub
  book-folder-b\
    book-b.epub
group2\
  book-folder-x\
    book-x.epub
```
1. edit `targets.txt` to contain a list of top-level folders to scan, one per
line. In this case it would be the full path to `group1` and `group2`.

1. run:
```
python ebook-analysis.py
```

# example output

As you can see from the output, this approach may have some data issues (i.g., State of the Art).
Possible improvements would be to attempt to select length-normalized chunks of
sentences from each book and run the algorithms on these chunks, rather than a
full-text scan of the extracted content.

```
python .\ebook-analysis.py
flesch  smog    dale-chall      book
84.78   7.7     6.06    Second Son - Lee Child
85.69   7.1     5.12    Worth Dying For - Lee Child
85.99   8.1     6.25    Deep Down - Lee Child
86.2    7.2     6.12    Not a Drill - Lee Child
86.3    7.0     5.71    High Heat - Lee Child
86.4    7.1     5.01    Tripwire - Lee Child
86.4    7.3     5.11    Never Go Back - Lee Child
86.81   7.3     4.99    The Affair - Lee Child
86.91   7.1     5.07    Nothing to Lose - Lee Child
87.01   7.2     5.07    Make Me - Lee Child
87.11   7.1     5.09    Bad Luck and Trouble - Lee Child
87.21   7.2     5.13    61 Hours - Lee Child
87.42   7.2     5.1     Gone Tomorrow - Lee Child
87.52   7.1     4.92    Without Fail - Lee Child
87.62   6.6     1.21    Echo Burning - Lee Child
87.62   7.4     5.99    Small Wars - Lee Child
87.72   6.8     1.21    Die Trying - Lee Child
87.72   6.8     4.88    The Enemy - Lee Child
87.82   6.8     1.23    Running Blind - Lee Child
88.02   7.3     5.02    Night School - Lee Child
96.48   6.5     1.16    Persuader - Lee Child
96.89   6.3     1.11    Killing Floor - Lee Child
71.04   10.3    5.63    Excession - Iain M. Banks
72.05   9.4     5.45    Matter - Iain M. Banks
72.36   9.8     5.45    The Algebraist - Iain M. Banks
72.76   9.6     5.33    Surface Detail - Iain M. Banks
74.19   9.0     5.52    Look to Windward - Iain M. Banks
78.18   8.7     6.2     A Song of Stone - Iain M. Banks
78.48   8.3     5.79    The Wasp Factory - Iain M. Banks
79.5    8.6     5.89    Feersum Endjinn - Iain M. Banks
79.9    9.1     5.61    Whit Or, Isis Amongst the Unsaved - Iain M. Banks
80.21   8.3     5.82    Complicity - Iain M. Banks
80.92   8.2     5.61    Walking on Glass - Iain M. Banks
80.92   9.3     5.61    Transition - Iain M. Banks
81.22   8.3     5.72    Espedair Street - Iain M. Banks
81.33   8.4     5.86    The Bridge - Iain M. Banks
81.73   8.1     5.76    Canal Dreams - Iain M. Banks
81.73   8.2     5.25    Consider Phlebas - Iain M. Banks
81.73   9.1     5.48    The Player of Games - Iain M. Banks
81.93   8.3     5.36    Inversions - Iain M. Banks
82.14   8.1     5.51    The Crow Road - Iain M. Banks
82.24   8.4     5.3     Against a Dark Background - Iain M. Banks
82.34   8.1     5.61    Stonemouth - Iain M. Banks
82.54   8.2     5.4     Use of Weapons - Iain M. Banks
83.46   8.5     5.69    The Business - Iain M. Banks
206.84  0.0     0.0     The State of the Art - Iain M. Banks
```