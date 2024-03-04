import FWCore.ParameterSet.Config as cms

def edmtest_global_TestBeginRunProducer(**kwargs):
  mod = cms.EDProducer('edmtest::global::TestBeginRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
