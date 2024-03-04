import FWCore.ParameterSet.Config as cms

def OuterTrackerMonitorTTTrack(**kwargs):
  mod = cms.EDProducer('OuterTrackerMonitorTTTrack',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
