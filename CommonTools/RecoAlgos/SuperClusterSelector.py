import FWCore.ParameterSet.Config as cms

def SuperClusterSelector(*args, **kwargs):
  mod = cms.EDFilter('SuperClusterSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
