import FWCore.ParameterSet.Config as cms

def PFSuperClusterReader(*args, **kwargs):
  mod = cms.EDAnalyzer('PFSuperClusterReader',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
