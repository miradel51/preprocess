# Convert_lowercase 
This simple script helps you to convert your each of sentence in the corpus into lowercase,uppercase or capitalize quickly. By the way, sometimes we need to convert our corpus into lowercase at once, in this case it helps you handle such a small problem in a minute. if u are not able to find the Perl script truecaser.perl which was provided in Moses, u can use this simple but effective python version of it.

# Usage
python convert_low.py input_file output_file

for instance, there is an english corpus called "training.en" need to be converted into lowercase via this script, input following command:

python convert_low.py ./training.en ./training.low.en

# Remove_sgm
This simple script helps you remove the &lt;sgm> format from your original parallel corpus.

Frequently, the open source resources which can be available from the WMT official website with <sgm> format, you need to remove these special tokens from the original corpus, then generate purely parallel corpus for training set, development set and test set.

In this case, you can use this script address such a problem via simple way as shown in this code.

# Usage

python remove_sgm.py input_file output_file

For instance, there are a pairs of parallel corpora called "newstest2017-deen-src.de.sgm" and "newstest2017-deen-ref.en.sgm" we need to remove or filter such special tokens from them. use following command:

python remove_sgm.py newstest2017-deen-ref.en.sgm newstest2017-deen-ref.en.no.sgm

# THULAC_seg
It is quite simple but efficient chinese word segmenter and it can be used in the preprocessing step in some NLP tasks if you need to chinese word segmentation. In this script we call the functions of the model was which provided by [THUNLP Group](http://nlp.csai.tsinghua.edu.cn/site2/index.php?lang=en), more precisely it was totally followed by [THULAC](https://github.com/thunlp/THULAC) open source project.

# Usage

Firslty，you have to install the [thulac](https://github.com/thunlp/THULAC) model, afterthat you are able to call the functions which can segment chinese sentence by line or by document via slightly change the code.

Secondly, according to your current demand, you can also change the original code slightly that coule be used in chinese segmentation sentence by sentence or line by line. If you use it with default style, it might be work with document level, as well as you will be able to segment chinse words by a whole document directly instead of line by line then save it.

Thirdly, it will be work shown as bellow:

For example, if there is a file ("training.5l.zh") which was included just 5 lines of chinese sentences, after processed you will be achieved an output file ("training.5l.zh.seg") with segmented style.

python thulac_seg.py ./training.5l.zh ./training.5l.zh.seg

