import FWCore.ParameterSet.Config as cms

def IsoTrackSelector(*args, **kwargs):
  mod = cms.EDFilter('IsoTrackSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
