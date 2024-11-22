import FWCore.ParameterSet.Config as cms

def TrackProducer(*args, **kwargs):
  mod = cms.EDProducer('TrackProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
