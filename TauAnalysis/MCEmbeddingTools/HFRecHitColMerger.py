import FWCore.ParameterSet.Config as cms

def HFRecHitColMerger(*args, **kwargs):
  mod = cms.EDProducer('HFRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
