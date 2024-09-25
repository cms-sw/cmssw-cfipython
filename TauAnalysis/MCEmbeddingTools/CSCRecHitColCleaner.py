import FWCore.ParameterSet.Config as cms

def CSCRecHitColCleaner(*args, **kwargs):
  mod = cms.EDProducer('CSCRecHitColCleaner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
