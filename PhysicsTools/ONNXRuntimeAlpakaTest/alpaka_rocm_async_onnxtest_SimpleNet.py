import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_onnxtest_SimpleNet(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::onnxtest::SimpleNet',
    model = cms.required.FileInPath,
    particles = cms.required.InputTag,
    featureMajor = cms.bool(False),
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
