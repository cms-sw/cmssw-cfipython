import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_btlrechit_BTLBaseRecHitSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::btlrechit::BTLBaseRecHitSoAProducer',
    digi = cms.required.InputTag,
    adcBitSaturation = cms.required.uint32,
    tclock = cms.required.double,
    tdcCalParams = cms.required.vdouble,
    qdcCalParams = cms.required.vdouble,
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
