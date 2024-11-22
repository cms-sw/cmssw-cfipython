import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestEndProcessBlockProducerNoGlobalCache(*args, **kwargs):
  mod = cms.EDProducer('edmtest::stream::TestEndProcessBlockProducerNoGlobalCache',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
