import FWCore.ParameterSet.Config as cms

def edmtest_FailingInLumiProducer(**kwargs):
  mod = cms.EDProducer('edmtest::FailingInLumiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
