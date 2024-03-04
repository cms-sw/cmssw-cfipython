import FWCore.ParameterSet.Config as cms

def edmtest_TransientIntParentProducer(**kwargs):
  mod = cms.EDProducer('edmtest::TransientIntParentProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
