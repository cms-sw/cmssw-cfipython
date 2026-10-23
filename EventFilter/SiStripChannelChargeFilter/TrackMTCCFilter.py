import FWCore.ParameterSet.Config as cms

def TrackMTCCFilter(*args, **kwargs):
  mod = cms.EDFilter('TrackMTCCFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
