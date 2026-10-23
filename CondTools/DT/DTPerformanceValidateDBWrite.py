import FWCore.ParameterSet.Config as cms

def DTPerformanceValidateDBWrite(*args, **kwargs):
  mod = cms.EDAnalyzer('DTPerformanceValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
