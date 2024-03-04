import FWCore.ParameterSet.Config as cms

def edmtest_global_StreamIntAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::global::StreamIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
