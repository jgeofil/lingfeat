# -*- coding: UTF-8 -*-
"""
Software: LingFeat - Comprehensive Linguistic Features for Readability Assessment
Page: VarF.py (Variational Features)
License: CC-BY-SA 4.0

Original Author: Bruce W. Lee (이웅성) @brucewlee
Affiliation 1: LXPER AI, Seoul, South Korea
Affiliation 2: University of Pennsylvania, PA, USA
Contributing Author: -
Affiliation : -


References:
>>> Variational features inspired by 
Publication 1: Lu, Xiaofei. "A corpus‐based evaluation of syntactic complexity measures as indices of college‐level ESL writers' language development." TESOL quarterly 45.1 (2011): 36-62.
Publication 2: Vajjala, Sowmya, and Detmar Meurers. "On improving the accuracy of readability classification using insights from second language acquisition." Proceedings of the seventh workshop on building educational applications using NLP. 2012.
"""
import math
from lingfeat.utils import division

def retrieve(NLP_doc):
    noun_list = []
    verb_list = []
    adje_list = []
    adve_list = []
    for token in NLP_doc:
        if token.pos_ == "ADJ":
            adje_list.append(token.lemma)
        elif token.pos_ == "ADV":
            adve_list.append(token.lemma)
        elif token.pos_ == "NOUN":
            noun_list.append(token.lemma)
        elif token.pos_ == "VERB":
            verb_list.append(token.lemma)
    n_unoun = sum(noun_list.count(noun) == 1 for noun in noun_list)
    n_uverb = sum(verb_list.count(verb) == 1 for verb in verb_list)
    n_uadje = sum(adje_list.count(adje) == 1 for adje in adje_list)
    n_uadve = sum(adve_list.count(adve) == 1 for adve in adve_list)
    return {
        "SimpNoV_S":float(division(n_unoun,(len(noun_list)))),
        "SquaNoV_S":float(division((n_unoun)**2,(len(noun_list)))),
        "CorrNoV_S":float(division(n_unoun,(math.sqrt(2*len(noun_list))))),
        "SimpVeV_S":float(division(n_uverb,(len(verb_list)))),
        "SquaVeV_S":float(division((n_uverb)**2,(len(verb_list)))),
        "CorrVeV_S":float(division(n_uverb,(math.sqrt(2*len(verb_list))))),
        "SimpAjV_S":float(division(n_uadje,(len(adje_list)))),
        "SquaAjV_S":float(division((n_uadje)**2,(len(adje_list)))),
        "CorrAjV_S":float(division(n_uadje,(math.sqrt(2*len(adje_list))))),
        "SimpAvV_S":float(division(n_uadve,(len(adve_list)))),
        "SquaAvV_S":float(division((n_uadve)**2,(len(adve_list)))),
        "CorrAvV_S":float(division(n_uadve,(math.sqrt(2*len(adve_list))))),
    }