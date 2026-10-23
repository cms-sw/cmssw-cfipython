import FWCore.ParameterSet.Config as cms

def FastTrackerRecHitMatcher(*args, **kwargs):
  mod = cms.EDProducer('FastTrackerRecHitMatcher',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
