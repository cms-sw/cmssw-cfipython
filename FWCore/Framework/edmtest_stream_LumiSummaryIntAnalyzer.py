import FWCore.ParameterSet.Config as cms

def edmtest_stream_LumiSummaryIntAnalyzer(**kwargs):
  mod = cms.EDAnalyzer('edmtest::stream::LumiSummaryIntAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
