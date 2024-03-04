import FWCore.ParameterSet.Config as cms

def ZDCRecHitColMerger(**kwargs):
  mod = cms.EDProducer('ZDCRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
