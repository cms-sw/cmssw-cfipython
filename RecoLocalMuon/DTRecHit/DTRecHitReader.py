import FWCore.ParameterSet.Config as cms

def DTRecHitReader(**kwargs):
  mod = cms.EDAnalyzer('DTRecHitReader',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
