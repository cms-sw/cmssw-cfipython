import FWCore.ParameterSet.Config as cms

def TrackingOfflineDQM(**kwargs):
  mod = cms.EDProducer('TrackingOfflineDQM',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
