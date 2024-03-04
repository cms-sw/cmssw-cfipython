import FWCore.ParameterSet.Config as cms

def edmtest_global_TestBeginProcessBlockProducer(**kwargs):
  mod = cms.EDProducer('edmtest::global::TestBeginProcessBlockProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
