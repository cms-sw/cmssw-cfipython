import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_MPISenderPortable(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::MPISenderPortable',
    upstream = cms.InputTag('source'),
    products = cms.VPSet(
      template = cms.PSetTemplate(
        type = cms.required.string,
        src = cms.required.InputTag
      )
    ),
    instance = cms.int32(0),
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
