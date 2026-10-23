import FWCore.ParameterSet.Config as cms

def DTPerformanceValidateDBRead(*args, **kwargs):
  mod = cms.EDAnalyzer('DTPerformanceValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
