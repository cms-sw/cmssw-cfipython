import FWCore.ParameterSet.Config as cms

def HTXSFilter(*args, **kwargs):
  mod = cms.EDFilter('HTXSFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
