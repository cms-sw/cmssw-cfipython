import FWCore.ParameterSet.Config as cms

def TrackCategorySelector(**kwargs):
  mod = cms.EDFilter('TrackCategorySelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
