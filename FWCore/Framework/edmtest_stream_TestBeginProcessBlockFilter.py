import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestBeginProcessBlockFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::stream::TestBeginProcessBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
