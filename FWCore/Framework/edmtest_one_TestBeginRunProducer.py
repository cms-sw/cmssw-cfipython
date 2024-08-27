import FWCore.ParameterSet.Config as cms

def edmtest_one_TestBeginRunProducer(**kwargs):
  mod = cms.EDProducer('edmtest::one::TestBeginRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
