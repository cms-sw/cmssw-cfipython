import FWCore.ParameterSet.Config as cms

def edmtest_limited_ProcessBlockIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::limited::ProcessBlockIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
