import FWCore.ParameterSet.Config as cms

def MuonBadTrackFilter(*args, **kwargs):
  mod = cms.EDFilter('MuonBadTrackFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
