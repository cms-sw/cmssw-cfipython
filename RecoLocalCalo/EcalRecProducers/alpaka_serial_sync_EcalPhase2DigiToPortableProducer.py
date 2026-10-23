import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_EcalPhase2DigiToPortableProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::EcalPhase2DigiToPortableProducer',
    BarrelDigis = cms.InputTag('simEcalUnsuppressedDigis'),
    digisLabelEB = cms.string('ebDigis'),
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
