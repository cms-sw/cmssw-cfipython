import FWCore.ParameterSet.Config as cms

def ExTestEcalTPGWeightGroupAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('ExTestEcalTPGWeightGroupAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
