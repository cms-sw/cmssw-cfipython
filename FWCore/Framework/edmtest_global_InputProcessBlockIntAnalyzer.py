import FWCore.ParameterSet.Config as cms

def edmtest_global_InputProcessBlockIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::global::InputProcessBlockIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
