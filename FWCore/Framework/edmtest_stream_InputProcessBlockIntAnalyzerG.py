import FWCore.ParameterSet.Config as cms

def edmtest_stream_InputProcessBlockIntAnalyzerG(**kwargs):
  mod = cms.EDAnalyzer('edmtest::stream::InputProcessBlockIntAnalyzerG',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod