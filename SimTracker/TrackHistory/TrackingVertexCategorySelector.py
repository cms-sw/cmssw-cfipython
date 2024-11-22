import FWCore.ParameterSet.Config as cms

def TrackingVertexCategorySelector(*args, **kwargs):
  mod = cms.EDFilter('TrackingVertexCategorySelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
