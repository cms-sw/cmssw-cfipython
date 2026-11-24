import FWCore.ParameterSet.Config as cms

def onnxtest_TinyResNet_alpaka(*args, **kwargs):
  mod = cms.EDProducer('onnxtest::TinyResNet@alpaka',
    model = cms.required.FileInPath,
    images = cms.required.InputTag,
    batchSize = cms.uint32(0),
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
