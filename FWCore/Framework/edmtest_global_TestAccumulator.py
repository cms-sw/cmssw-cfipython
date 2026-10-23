import FWCore.ParameterSet.Config as cms

def edmtest_global_TestAccumulator(*args, **kwargs):
  mod = cms.EDProducer('edmtest::global::TestAccumulator',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
