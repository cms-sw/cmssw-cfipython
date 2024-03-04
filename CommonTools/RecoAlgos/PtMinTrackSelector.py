import FWCore.ParameterSet.Config as cms

def PtMinTrackSelector(**kwargs):
  mod = cms.EDFilter('PtMinTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
