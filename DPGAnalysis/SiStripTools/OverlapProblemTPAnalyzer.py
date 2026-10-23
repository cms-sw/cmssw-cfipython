import FWCore.ParameterSet.Config as cms

def OverlapProblemTPAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('OverlapProblemTPAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
