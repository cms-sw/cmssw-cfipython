import FWCore.ParameterSet.Config as cms

def edmtest_one_ProcessBlockIntProducer(**kwargs):
  mod = cms.EDProducer('edmtest::one::ProcessBlockIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
