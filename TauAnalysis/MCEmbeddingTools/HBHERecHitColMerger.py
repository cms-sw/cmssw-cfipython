import FWCore.ParameterSet.Config as cms

def HBHERecHitColMerger(*args, **kwargs):
  mod = cms.EDProducer('HBHERecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
