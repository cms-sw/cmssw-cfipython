import FWCore.ParameterSet.Config as cms

def torchtest_SimpleNet_alpaka(*args, **kwargs):
  mod = cms.EDProducer('torchtest::SimpleNet@alpaka',
    model = cms.required.FileInPath,
    convertToFP16 = cms.required.bool,
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
