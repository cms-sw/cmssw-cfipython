import FWCore.ParameterSet.Config as cms

def ByClusterSummaryMultiplicityPairEventFilter(*args, **kwargs):
  mod = cms.EDFilter('ByClusterSummaryMultiplicityPairEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
