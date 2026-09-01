import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_ngt_GenericClonerPortable(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::ngt::GenericClonerPortable',
    products = cms.VPSet(
      template = cms.PSetTemplate(
        type = cms.required.string,
        src = cms.required.InputTag
      )
    ),
    verbose = cms.untracked.bool(False),
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
