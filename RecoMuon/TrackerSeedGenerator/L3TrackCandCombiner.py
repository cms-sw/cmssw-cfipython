import FWCore.ParameterSet.Config as cms

def L3TrackCandCombiner(**kwargs):
  mod = cms.EDProducer('L3TrackCandCombiner',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
