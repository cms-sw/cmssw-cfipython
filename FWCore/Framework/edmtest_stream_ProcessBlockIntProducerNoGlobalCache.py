import FWCore.ParameterSet.Config as cms

def edmtest_stream_ProcessBlockIntProducerNoGlobalCache(**kwargs):
  mod = cms.EDProducer('edmtest::stream::ProcessBlockIntProducerNoGlobalCache',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
