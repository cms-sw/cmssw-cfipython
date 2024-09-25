import FWCore.ParameterSet.Config as cms

def TauValGenPSelector(*args, **kwargs):
  mod = cms.EDFilter('TauValGenPSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
