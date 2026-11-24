import FWCore.ParameterSet.Config as cms

def onnxtest_ScaledNet_alpaka(*args, **kwargs):
  mod = cms.EDProducer('onnxtest::ScaledNet@alpaka',
    model = cms.required.FileInPath,
    batchSize = cms.uint32(0),
    hits = cms.required.InputTag,
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
