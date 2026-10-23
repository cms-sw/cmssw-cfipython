import FWCore.ParameterSet.Config as cms

def edmtest_stream_GlobalIntAnalyzer(*args, **kwargs):
  mod = cms.EDAnalyzer('edmtest::stream::GlobalIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
