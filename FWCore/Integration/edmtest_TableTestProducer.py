import FWCore.ParameterSet.Config as cms

def edmtest_TableTestProducer(**kwargs):
  mod = cms.EDProducer('edmtest::TableTestProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
