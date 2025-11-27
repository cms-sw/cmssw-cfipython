import FWCore.ParameterSet.Config as cms

def torchtest_DataSource_alpaka(*args, **kwargs):
  mod = cms.EDProducer('torchtest::DataSource@alpaka',
    batchSize = cms.required.uint32,
    environment = cms.untracked.int32(0),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string(''),
      synchronize = cms.optional.untracked.bool
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
