import FWCore.ParameterSet.Config as cms

def DTPerformanceValidateDBRead(**kwargs):
  mod = cms.EDAnalyzer('DTPerformanceValidateDBRead',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
