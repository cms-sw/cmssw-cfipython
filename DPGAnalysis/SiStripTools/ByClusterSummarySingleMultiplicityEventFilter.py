import FWCore.ParameterSet.Config as cms

def ByClusterSummarySingleMultiplicityEventFilter(*args, **kwargs):
  mod = cms.EDFilter('ByClusterSummarySingleMultiplicityEventFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
