import FWCore.ParameterSet.Config as cms

def edmtest_global_RunSummaryIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::global::RunSummaryIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
