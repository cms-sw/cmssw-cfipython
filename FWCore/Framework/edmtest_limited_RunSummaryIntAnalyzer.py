import FWCore.ParameterSet.Config as cms

def edmtest_limited_RunSummaryIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::limited::RunSummaryIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
