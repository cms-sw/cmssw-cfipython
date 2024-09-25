import FWCore.ParameterSet.Config as cms

def TrackInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackInfoProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
