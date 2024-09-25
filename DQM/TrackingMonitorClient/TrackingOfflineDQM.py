import FWCore.ParameterSet.Config as cms

def TrackingOfflineDQM(*args, **kwargs):
  mod = cms.EDProducer('TrackingOfflineDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
