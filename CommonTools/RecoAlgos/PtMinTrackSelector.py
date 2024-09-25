import FWCore.ParameterSet.Config as cms

def PtMinTrackSelector(*args, **kwargs):
  mod = cms.EDFilter('PtMinTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
