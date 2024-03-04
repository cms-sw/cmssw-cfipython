import FWCore.ParameterSet.Config as cms

def OuterTrackerMonitorTTCluster(**kwargs):
  mod = cms.EDProducer('OuterTrackerMonitorTTCluster',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
