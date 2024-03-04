import FWCore.ParameterSet.Config as cms

def edmtest_limited_StreamIntAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::limited::StreamIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
