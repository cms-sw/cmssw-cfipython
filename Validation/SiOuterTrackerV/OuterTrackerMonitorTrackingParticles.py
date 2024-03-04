import FWCore.ParameterSet.Config as cms

def OuterTrackerMonitorTrackingParticles(**kwargs):
  mod = cms.EDProducer('OuterTrackerMonitorTrackingParticles',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
