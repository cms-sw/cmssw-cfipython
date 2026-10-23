import FWCore.ParameterSet.Config as cms

def edmtest_MissingDictionaryCUDAProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::MissingDictionaryCUDAProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
