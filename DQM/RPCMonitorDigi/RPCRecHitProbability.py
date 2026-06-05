import FWCore.ParameterSet.Config as cms

def RPCRecHitProbability(*args, **kwargs):
  mod = cms.EDProducer('RPCRecHitProbability',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
