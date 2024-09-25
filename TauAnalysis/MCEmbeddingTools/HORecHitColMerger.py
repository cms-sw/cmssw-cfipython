import FWCore.ParameterSet.Config as cms

def HORecHitColMerger(*args, **kwargs):
  mod = cms.EDProducer('HORecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
