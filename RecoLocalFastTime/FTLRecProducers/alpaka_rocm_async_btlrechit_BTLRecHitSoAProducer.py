import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_btlrechit_BTLRecHitSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::btlrechit::BTLRecHitSoAProducer',
    baserh = cms.required.InputTag,
    invLightSpeedLYSO = cms.required.double,
    thresholdToKeep = cms.required.double,
    calibrationConstant = cms.required.double,
    npeSaturationCorr = cms.required.vdouble,
    npeToADC = cms.required.vdouble,
    npePerGeV = cms.required.double,
    timeCalibrationConstant = cms.required.double,
    tResParams = cms.required.vdouble,
    twcParams = cms.required.vdouble,
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
