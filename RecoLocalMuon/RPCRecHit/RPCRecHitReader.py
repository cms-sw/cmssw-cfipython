import FWCore.ParameterSet.Config as cms

def RPCRecHitReader(*args, **kwargs):
  mod = cms.EDAnalyzer('RPCRecHitReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
