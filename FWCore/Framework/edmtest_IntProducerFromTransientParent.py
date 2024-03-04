import FWCore.ParameterSet.Config as cms

def edmtest_IntProducerFromTransientParent(**kwargs):
  mod = cms.EDProducer('edmtest::IntProducerFromTransientParent',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
