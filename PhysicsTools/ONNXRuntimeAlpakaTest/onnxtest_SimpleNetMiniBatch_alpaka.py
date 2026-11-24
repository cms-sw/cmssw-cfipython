import FWCore.ParameterSet.Config as cms

def onnxtest_SimpleNetMiniBatch_alpaka(*args, **kwargs):
  mod = cms.EDProducer('onnxtest::SimpleNetMiniBatch@alpaka',
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
