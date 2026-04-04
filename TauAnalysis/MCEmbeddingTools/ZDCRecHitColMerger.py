import FWCore.ParameterSet.Config as cms

def ZDCRecHitColMerger(*args, **kwargs):
  mod = cms.EDProducer('ZDCRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
