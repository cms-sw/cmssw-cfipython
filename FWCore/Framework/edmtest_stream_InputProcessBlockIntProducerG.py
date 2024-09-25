import FWCore.ParameterSet.Config as cms

def edmtest_stream_InputProcessBlockIntProducerG(*args, **kwargs):
  mod = cms.EDProducer('edmtest::stream::InputProcessBlockIntProducerG',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
