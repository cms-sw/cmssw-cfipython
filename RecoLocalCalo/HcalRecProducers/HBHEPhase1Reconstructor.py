import FWCore.ParameterSet.Config as cms

def HBHEPhase1Reconstructor(**kwargs):
  mod = cms.EDProducer('HBHEPhase1Reconstructor',
    digiLabelQIE8 = cms.required.InputTag,
    digiLabelQIE11 = cms.required.InputTag,
    algoConfigClass = cms.required.string,
    processQIE8 = cms.required.bool,
    processQIE11 = cms.required.bool,
    saveInfos = cms.required.bool,
    saveDroppedInfos = cms.required.bool,
    makeRecHits = cms.required.bool,
    dropZSmarkedPassed = cms.required.bool,
    tsFromDB = cms.required.bool,
    recoParamsFromDB = cms.required.bool,
    saveEffectivePedestal = cms.bool(False),
    use8ts = cms.bool(False),
    sipmQTSShift = cms.int32(0),
    sipmQNTStoSum = cms.int32(3),
    setNegativeFlagsQIE8 = cms.required.bool,
    setNegativeFlagsQIE11 = cms.required.bool,
    setNoiseFlagsQIE8 = cms.required.bool,
    setNoiseFlagsQIE11 = cms.required.bool,
    setPulseShapeFlagsQIE8 = cms.required.bool,
    setPulseShapeFlagsQIE11 = cms.required.bool,
    setLegacyFlagsQIE8 = cms.required.bool,
    setLegacyFlagsQIE11 = cms.required.bool,
    algorithm = cms.PSet(
      Class = cms.string('SimpleHBHEPhase1Algo'),
      useM2 = cms.bool(False),
      useM3 = cms.bool(True),
      useMahi = cms.bool(True),
      firstSampleShift = cms.int32(0),
      samplesToAdd = cms.int32(2),
      correctionPhaseNS = cms.double(6),
      tdcTimeShift = cms.double(0),
      correctForPhaseContainment = cms.bool(True),
      applyLegacyHBMCorrection = cms.bool(True),
      calculateArrivalTime = cms.bool(False),
      timeAlgo = cms.int32(1),
      thEnergeticPulses = cms.double(5),
      applyFixPCC = cms.bool(False)
    ),
    flagParametersQIE8 = cms.PSet(),
    flagParametersQIE11 = cms.PSet(),
    pulseShapeParametersQIE8 = cms.PSet(),
    pulseShapeParametersQIE11 = cms.PSet(),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
