import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestBeginLumiBlockFilter(**kwargs):
  mod = cms.EDFilter('edmtest::stream::TestBeginLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
