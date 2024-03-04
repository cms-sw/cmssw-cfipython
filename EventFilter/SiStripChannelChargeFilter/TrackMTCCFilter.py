import FWCore.ParameterSet.Config as cms

def TrackMTCCFilter(**kwargs):
  mod = cms.EDFilter('TrackMTCCFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
