import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_torchtest_MultiHeadNet(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::torchtest::MultiHeadNet',
    model = cms.required.FileInPath,
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
