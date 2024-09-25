import FWCore.ParameterSet.Config as cms

def edmtest_IntProducerFromTransientParent(*args, **kwargs):
  mod = cms.EDProducer('edmtest::IntProducerFromTransientParent',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
