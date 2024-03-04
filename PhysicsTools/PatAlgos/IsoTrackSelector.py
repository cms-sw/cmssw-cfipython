import FWCore.ParameterSet.Config as cms

def IsoTrackSelector(**kwargs):
  mod = cms.EDFilter('IsoTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
