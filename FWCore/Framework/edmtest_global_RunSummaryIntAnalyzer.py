import FWCore.ParameterSet.Config as cms

def edmtest_global_RunSummaryIntAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::global::RunSummaryIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
