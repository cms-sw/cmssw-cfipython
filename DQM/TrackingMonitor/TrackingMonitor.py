import FWCore.ParameterSet.Config as cms

def TrackingMonitor(**kwargs):
  mod = cms.EDProducer('TrackingMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
