import FWCore.ParameterSet.Config as cms

def TrackSelector(**kwargs):
  mod = cms.EDFilter('TrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
