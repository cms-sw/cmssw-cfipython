import FWCore.ParameterSet.Config as cms

def TrackCategorySelector(*args, **kwargs):
  mod = cms.EDFilter('TrackCategorySelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
