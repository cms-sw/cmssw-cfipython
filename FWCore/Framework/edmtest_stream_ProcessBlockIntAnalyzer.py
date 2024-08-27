import FWCore.ParameterSet.Config as cms

def edmtest_stream_ProcessBlockIntAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::stream::ProcessBlockIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
