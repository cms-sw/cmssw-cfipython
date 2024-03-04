import FWCore.ParameterSet.Config as cms

def ByClusterSummarySingleMultiplicityEventFilter(**kwargs):
  mod = cms.EDFilter('ByClusterSummarySingleMultiplicityEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
