import FWCore.ParameterSet.Config as cms

def edmtest_one_TestBeginLumiBlockProducer(**kwargs):
  mod = cms.EDProducer('edmtest::one::TestBeginLumiBlockProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
