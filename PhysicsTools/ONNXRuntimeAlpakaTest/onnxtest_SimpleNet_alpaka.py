import FWCore.ParameterSet.Config as cms

def onnxtest_SimpleNet_alpaka(*args, **kwargs):
  mod = cms.EDProducer('onnxtest::SimpleNet@alpaka',
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
