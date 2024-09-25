import FWCore.ParameterSet.Config as cms

def PFClusterAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('PFClusterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
