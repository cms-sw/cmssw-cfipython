import FWCore.ParameterSet.Config as cms

def edmtest_global_LumiIntAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::global::LumiIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
