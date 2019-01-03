# word embedding models

## fasttext skipgram with 100 dimension 

this model created on wiki corpus by fasttext. the command which build model for me:

`./fasttext skipgram -input data.txt -output model`

I tested this model in analogy and similarity test.

## analogy result:

first column is category , second column is total number of questions in each category and third column is number of correct answers 

semantic-capitals,4691,3514

semantic-Whole to part,420,68

syntactic-Comparative Adjectives,2756,1927

syntactic-antonym,506,239

semantic-family,600,349

semantic-currency,6006,1298

syntactic-Superlative Adjectives,2756,1611

syntactic-verb,1964,708

## similarity results:

### spearman rate:

for sematic similarity dataset: 0.48587616530876959

for farsnet semantic similarity dataset :

FarsnetSim1:0.27610083415580711

FarsnetSim2:0.27929982329748931

wup:0.18250087600972492

jcn:0.18327200031556271

vector:0.13933219280879294

vector pairwise:0.018409448914572579

res:0.13439418289866359

lin:0.20054370309396596

path:0.18463631191518065

lch:0.18463631191518065

hso:0.094630984814642702

lesk:0.10516558436396144



### pearson rate:

for sematic similarity dataset: 0.48469245154228224

for farsnet semantic similarity dataset :

FarsnetSim1:0.061106823597353102

FarsnetSim2:0.062575233204542127

wup:0.077740945428833419

jcn:0.21993964374043662

vector:-0.053878808327336804

vector pairwise:-0.00032728115126094031

res:0.2600105151984291

lin:0.12138530521845443

path:0.10809710152907191

lch:0.11427292317594209

hso:0.17404572114709974

lesk:0.10938928805987569

