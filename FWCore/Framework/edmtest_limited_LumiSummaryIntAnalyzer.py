import FWCore.ParameterSet.Config as cms

def edmtest_limited_LumiSummaryIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::limited::LumiSummaryIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
