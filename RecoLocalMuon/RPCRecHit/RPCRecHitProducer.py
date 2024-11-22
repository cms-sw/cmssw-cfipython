import FWCore.ParameterSet.Config as cms

def RPCRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('RPCRecHitProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
