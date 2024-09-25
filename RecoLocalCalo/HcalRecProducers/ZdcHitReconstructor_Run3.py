import FWCore.ParameterSet.Config as cms

def ZdcHitReconstructor_Run3(*args, **kwargs):
  mod = cms.EDProducer('ZdcHitReconstructor_Run3',
    digiLabelQIE10ZDC = cms.InputTag('hcalDigis', 'ZDC'),
    Subdetector = cms.string('ZDC'),
    dropZSmarkedPassed = cms.bool(True),
    skipRPD = cms.bool(True),
    recoMethod = cms.int32(1),
    correctionMethodEM = cms.int32(1),
    correctionMethodHAD = cms.int32(1),
    correctionMethodRPD = cms.int32(0),
    ootpuRatioEM = cms.double(3),
    ootpuRatioHAD = cms.double(3),
    ootpuRatioRPD = cms.double(-1),
    ootpuFracEM = cms.double(1),
    ootpuFracHAD = cms.double(1),
    ootpuFracRPD = cms.double(0),
    chargeRatiosEM = cms.vdouble(
      1,
      0.23157,
      0.10477,
      0.06312
    ),
    chargeRatiosHAD = cms.vdouble(
      1,
      0.23157,
      0.10477,
      0.06312
    ),
    chargeRatiosRPD = cms.vdouble(
      1,
      0.23157,
      0.10477,
      0.06312
    ),
    bxTs = cms.vuint32(
      0,
      2,
      4
    ),
    nTs = cms.int32(6),
    forceSOI = cms.bool(False),
    signalSOI = cms.vuint32(2),
    noiseSOI = cms.vuint32(1),
    setSaturationFlags = cms.bool(False),
    saturationParameters = cms.PSet(
      maxADCvalue = cms.int32(255)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
