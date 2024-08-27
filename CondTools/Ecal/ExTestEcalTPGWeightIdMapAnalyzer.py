import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGWeightIdMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGWeightIdMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
