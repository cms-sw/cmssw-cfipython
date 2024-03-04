import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestEndLumiBlockFilter(**kwargs):
  mod = cms.EDFilter('edmtest::stream::TestEndLumiBlockFilter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
