import FWCore.ParameterSet.Config as cms

def HBHERecHitColMerger(**kwargs):
  mod = cms.EDProducer('HBHERecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
