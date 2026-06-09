import FWCore.ParameterSet.Config as cms

def TrackingMonitor(*args, **kwargs):
  mod = cms.EDProducer('TrackingMonitor',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
