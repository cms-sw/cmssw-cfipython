import FWCore.ParameterSet.Config as cms

def edmtest_MaybeUninitializedIntProducer(*args, **kwargs):
  mod = cms.EDProducer('edmtest::MaybeUninitializedIntProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
