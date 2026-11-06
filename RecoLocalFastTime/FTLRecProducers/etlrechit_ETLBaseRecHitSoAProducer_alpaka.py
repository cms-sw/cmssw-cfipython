import FWCore.ParameterSet.Config as cms

def etlrechit_ETLBaseRecHitSoAProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('etlrechit::ETLBaseRecHitSoAProducer@alpaka',
    digi = cms.required.InputTag,
    adcNbits = cms.required.uint32,
    adcSaturation = cms.required.double,
    toaLSB_ns = cms.required.double,
    tdcWindowStart = cms.required.double,
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
