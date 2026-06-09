import FWCore.ParameterSet.Config as cms

def FastTrackerRecHitMaskProducer(*args, **kwargs):
  mod = cms.EDProducer('FastTrackerRecHitMaskProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
