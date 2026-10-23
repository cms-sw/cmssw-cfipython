import FWCore.ParameterSet.Config as cms

def PFSuperClusterTreeMaker(*args, **kwargs):
  mod = cms.EDAnalyzer('PFSuperClusterTreeMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
