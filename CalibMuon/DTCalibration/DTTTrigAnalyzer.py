import FWCore.ParameterSet.Config as cms

def DTTTrigAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('DTTTrigAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
