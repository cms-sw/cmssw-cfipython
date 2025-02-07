import FWCore.ParameterSet.Config as cms

def edmtest_global_RunSummaryIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::global::RunSummaryIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
