import FWCore.ParameterSet.Config as cms

def TrackRefSelector(*args, **kwargs):
  mod = cms.EDFilter('TrackRefSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
