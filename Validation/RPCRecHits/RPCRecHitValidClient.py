import FWCore.ParameterSet.Config as cms

def RPCRecHitValidClient(*args, **kwargs):
  mod = cms.EDProducer('RPCRecHitValidClient',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
