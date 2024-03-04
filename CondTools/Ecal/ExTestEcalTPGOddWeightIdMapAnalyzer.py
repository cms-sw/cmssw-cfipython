import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGOddWeightIdMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGOddWeightIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
