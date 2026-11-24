import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_onnxtest_SimpleNetMiniBatch(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::onnxtest::SimpleNetMiniBatch',
    model = cms.required.FileInPath,
    batchSize = cms.required.uint32,
    particles = cms.required.InputTag,
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
