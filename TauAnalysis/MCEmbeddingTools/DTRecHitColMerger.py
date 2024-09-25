import FWCore.ParameterSet.Config as cms

def DTRecHitColMerger(*args, **kwargs):
  mod = cms.EDProducer('DTRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
