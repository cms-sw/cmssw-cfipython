import FWCore.ParameterSet.Config as cms

def MCVerticesWeight(*args, **kwargs):
  mod = cms.EDFilter('MCVerticesWeight',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
