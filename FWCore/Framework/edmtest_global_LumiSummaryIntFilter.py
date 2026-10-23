import FWCore.ParameterSet.Config as cms

def edmtest_global_LumiSummaryIntFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::global::LumiSummaryIntFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
