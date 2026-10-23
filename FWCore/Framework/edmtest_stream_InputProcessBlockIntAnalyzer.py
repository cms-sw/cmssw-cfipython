import FWCore.ParameterSet.Config as cms

def edmtest_stream_InputProcessBlockIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::stream::InputProcessBlockIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
