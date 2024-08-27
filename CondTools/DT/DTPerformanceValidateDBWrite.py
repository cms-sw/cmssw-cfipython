import FWCore.ParameterSet.Config as cms

def DTPerformanceValidateDBWrite(**kwargs):
  mod = cms.EDAnalyzer('DTPerformanceValidateDBWrite',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
