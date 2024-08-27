import FWCore.ParameterSet.Config as cms

def edmtest_FailingInRunProducer(**kwargs):
  mod = cms.EDProducer('edmtest::FailingInRunProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
