import FWCore.ParameterSet.Config as cms

def ByClusterSummaryMultiplicityPairEventFilter(**kwargs):
  mod = cms.EDFilter('ByClusterSummaryMultiplicityPairEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
