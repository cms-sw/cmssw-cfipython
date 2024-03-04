import FWCore.ParameterSet.Config as cms

def EcalTBWeightsAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalTBWeightsAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
