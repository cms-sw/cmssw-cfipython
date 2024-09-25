import FWCore.ParameterSet.Config as cms

def TrackFullCloneSelector(*args, **kwargs):
  mod = cms.EDFilter('TrackFullCloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
