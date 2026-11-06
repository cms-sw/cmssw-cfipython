import FWCore.ParameterSet.Config as cms

def btlrechit_BTLBaseRecHitSoAProducer_alpaka(*args, **kwargs):
  mod = cms.EDProducer('btlrechit::BTLBaseRecHitSoAProducer@alpaka',
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
