# Convert_lowercase 
This simple script helps you to convert your each of sentence in the corpus into lowercase,uppercase or capitalize quickly. By the way, sometimes we need to convert our corpus into lowercase at once, in this case it helps you handle such a small problem in a minute. if u are not able to find the Perl script truecaser.perl which was provided in Moses, u can use this simple but effective python version of it.

# Usage
python convert_low.py input_file output_file

for instance, there is an english corpus called "training.en" need to be converted into lowercase via this script, input following command:

python convert_low,py ./training.en ./training.low.en

# Remove_sgm
This simple script helps you remove the &lt;sgm> format from your original parallel corpus.

Frequently, the open source resources which can be available from the WMT official website with <sgm> format, you need to remove these special tokens from the original corpus, then generate purely parallel corpus for training set, development set and test set.

In this case, you can use this script address such a problem via simple way as shown in this code.

# Usage

python remove_sgm.py input_file output_file

For instance, there are a pairs of parallel corpora called "newstest2017-deen-src.de.sgm" and "newstest2017-deen-ref.en.sgm" we need to remove or filter such special tokens from them. use following command:

python remove_sgm.py newstest2017-deen-ref.en.sgm newstest2017-deen-ref.en.no.sgm
