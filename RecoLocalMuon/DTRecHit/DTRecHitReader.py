import FWCore.ParameterSet.Config as cms

def DTRecHitReader(*args, **kwargs):
  mod = cms.EDAnalyzer('DTRecHitReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
