import FWCore.ParameterSet.Config as cms

def MuonBadTrackFilter(**kwargs):
  mod = cms.EDFilter('MuonBadTrackFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
