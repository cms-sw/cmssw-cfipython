import FWCore.ParameterSet.Config as cms

def RPCRecHitColMerger(**kwargs):
  mod = cms.EDProducer('RPCRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
