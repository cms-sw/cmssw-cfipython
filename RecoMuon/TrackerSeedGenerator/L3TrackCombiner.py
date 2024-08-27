import FWCore.ParameterSet.Config as cms

def L3TrackCombiner(**kwargs):
  mod = cms.EDProducer('L3TrackCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
