import FWCore.ParameterSet.Config as cms

def DTTTrigWriter(**kwargs):
  mod = cms.EDAnalyzer('DTTTrigWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
