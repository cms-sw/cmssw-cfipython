import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_onnxtest_MaskedNet(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::onnxtest::MaskedNet',
    model = cms.required.FileInPath,
    particles = cms.required.InputTag,
    reverseOrder = cms.bool(False),
    emptyMask = cms.bool(False),
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
