import FWCore.ParameterSet.Config as cms

def ProbClustersFilter(**kwargs):
  mod = cms.EDFilter('ProbClustersFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
