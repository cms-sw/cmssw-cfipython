import FWCore.ParameterSet.Config as cms

def CSCRecHitColMerger(*args, **kwargs):
  mod = cms.EDProducer('CSCRecHitColMerger',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
