import FWCore.ParameterSet.Config as cms

def FastTrackerRecHitMaskFromSeedProducer(*args, **kwargs):
  mod = cms.EDProducer('FastTrackerRecHitMaskFromSeedProducer',
    trajectories = cms.InputTag('initialStepSeeds'),
    recHits = cms.InputTag('fastTrackerRecHits'),
    oldHitRemovalInfo = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
