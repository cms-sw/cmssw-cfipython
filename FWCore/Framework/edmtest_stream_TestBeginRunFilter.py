import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestBeginRunFilter(*args, **kwargs):
  mod = cms.EDFilter('edmtest::stream::TestBeginRunFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
