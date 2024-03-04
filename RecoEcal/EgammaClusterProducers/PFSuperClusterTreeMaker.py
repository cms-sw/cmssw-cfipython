import FWCore.ParameterSet.Config as cms

def PFSuperClusterTreeMaker(**kwargs):
  mod = cms.EDAnalyzer('PFSuperClusterTreeMaker',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
