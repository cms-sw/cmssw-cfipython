import FWCore.ParameterSet.Config as cms

def HORecHitColMerger(**kwargs):
  mod = cms.EDProducer('HORecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
