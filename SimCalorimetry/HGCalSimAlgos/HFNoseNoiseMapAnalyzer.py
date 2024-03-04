import FWCore.ParameterSet.Config as cms

def HFNoseNoiseMapAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('HFNoseNoiseMapAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
