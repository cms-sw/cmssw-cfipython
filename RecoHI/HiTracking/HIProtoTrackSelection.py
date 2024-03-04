import FWCore.ParameterSet.Config as cms

def HIProtoTrackSelection(**kwargs):
  mod = cms.EDFilter('HIProtoTrackSelection',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
