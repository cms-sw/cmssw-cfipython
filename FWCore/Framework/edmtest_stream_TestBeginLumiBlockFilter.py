import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestBeginLumiBlockFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::stream::TestBeginLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
