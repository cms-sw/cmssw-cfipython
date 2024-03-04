import FWCore.ParameterSet.Config as cms

def DTRecHitColMerger(**kwargs):
  mod = cms.EDProducer('DTRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
