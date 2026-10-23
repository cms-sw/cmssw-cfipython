import FWCore.ParameterSet.Config as cms

def TrackTimeValueMapProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackTimeValueMapProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
