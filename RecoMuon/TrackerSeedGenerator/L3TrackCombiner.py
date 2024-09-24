import FWCore.ParameterSet.Config as cms

def L3TrackCombiner(*args, **kwargs):
  mod = cms.EDProducer('L3TrackCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
