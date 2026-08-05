import FWCore.ParameterSet.Config as cms

def HTXSStage1p2Filter(*args, **kwargs):
  mod = cms.EDFilter('HTXSStage1p2Filter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
