import FWCore.ParameterSet.Config as cms

def edmtest_global_InputProcessBlockAnalyzerReuseCache(**kwargs):
  mod = cms.EDAnalyzer('edmtest::global::InputProcessBlockAnalyzerReuseCache',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
