import FWCore.ParameterSet.Config as cms

def EcalGainRatiosAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('EcalGainRatiosAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
