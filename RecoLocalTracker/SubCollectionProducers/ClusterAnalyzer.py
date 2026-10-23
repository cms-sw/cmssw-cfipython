import FWCore.ParameterSet.Config as cms

def ClusterAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('ClusterAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
