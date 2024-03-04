import FWCore.ParameterSet.Config as cms

def TrackRefSelector(**kwargs):
  mod = cms.EDFilter('TrackRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
