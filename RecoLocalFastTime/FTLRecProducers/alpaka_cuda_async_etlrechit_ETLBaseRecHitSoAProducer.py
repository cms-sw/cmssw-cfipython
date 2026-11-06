import FWCore.ParameterSet.Config as cms

def alpaka_cuda_async_etlrechit_ETLBaseRecHitSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_cuda_async::etlrechit::ETLBaseRecHitSoAProducer',
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
