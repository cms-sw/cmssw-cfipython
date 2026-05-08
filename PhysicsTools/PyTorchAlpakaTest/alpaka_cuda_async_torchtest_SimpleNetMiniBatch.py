import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_torchtest_SimpleNetMiniBatch(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::torchtest::SimpleNetMiniBatch',
    model = cms.required.FileInPath,
    batchSize = cms.required.int32,
    particles = cms.required.InputTag,
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
