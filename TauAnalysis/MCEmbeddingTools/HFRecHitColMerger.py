import FWCore.ParameterSet.Config as cms

def HFRecHitColMerger(**kwargs):
  mod = cms.EDProducer('HFRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
