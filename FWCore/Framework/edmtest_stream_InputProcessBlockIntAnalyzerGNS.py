import FWCore.ParameterSet.Config as cms

def edmtest_stream_InputProcessBlockIntAnalyzerGNS(**kwargs):
  mod = cms.EDAnalyzer('edmtest::stream::InputProcessBlockIntAnalyzerGNS',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
