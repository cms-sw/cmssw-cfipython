import FWCore.ParameterSet.Config as cms

def RPCRecHitValid(*args, **kwargs):
  mod = cms.EDProducer('RPCRecHitValid',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
