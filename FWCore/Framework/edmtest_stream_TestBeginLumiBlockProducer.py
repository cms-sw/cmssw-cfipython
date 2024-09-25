import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestBeginLumiBlockProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::stream::TestBeginLumiBlockProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
