import FWCore.ParameterSet.Config as cms

def PFClusterAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('PFClusterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
