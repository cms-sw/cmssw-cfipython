import FWCore.ParameterSet.Config as cms

def allocMonTest_TransformAsyncAllocProducer(*args, **kwargs):
  mod = cms.EDProducer('allocMonTest::TransformAsyncAllocProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
