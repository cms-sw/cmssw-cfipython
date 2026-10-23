import FWCore.ParameterSet.Config as cms

def torchtest_TinyResNetMiniBatch_alpaka(*args, **kwargs):
  mod = cms.EDProducer('torchtest::TinyResNetMiniBatch@alpaka',
    model = cms.required.FileInPath,
    batchSize = cms.required.int32,
    images = cms.required.InputTag,
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
