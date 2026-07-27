import FWCore.ParameterSet.Config as cms

def allocMonTest_ExternalWorkTransformAllocProducer(*args, **kwargs):
  mod = cms.EDProducer('allocMonTest::ExternalWorkTransformAllocProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
