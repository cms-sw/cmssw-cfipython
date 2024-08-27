import FWCore.ParameterSet.Config as cms

def TrackFullCloneSelector(**kwargs):
  mod = cms.EDFilter('TrackFullCloneSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
