import FWCore.ParameterSet.Config as cms

def CastorRecHitColMerger(**kwargs):
  mod = cms.EDProducer('CastorRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
