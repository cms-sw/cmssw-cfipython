import FWCore.ParameterSet.Config as cms

def edmtest_stream_TestEndRunProducer(**kwargs):
  mod = cms.EDProducer('edmtest::stream::TestEndRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
