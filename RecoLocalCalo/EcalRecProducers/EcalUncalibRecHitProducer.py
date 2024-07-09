import FWCore.ParameterSet.Config as cms

def EcalUncalibRecHitProducer(**kwargs):
  mod = cms.EDProducer('EcalUncalibRecHitProducer',
    EBdigiCollection = cms.InputTag('ecalDigis', 'ebDigis'),
    EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
    EEdigiCollection = cms.InputTag('ecalDigis', 'eeDigis'),
    EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
    algo = cms.string('EcalUncalibRecHitWorkerMultiFit'),
    algoPSet = cms.PSet(
      activeBXs = cms.vint32(
        -5,
        -4,
        -3,
        -2,
        -1,
        0,
        1,
        2,
        3,
        4
      ),
      ampErrorCalculation = cms.bool(True),
      useLumiInfoRunHeader = cms.bool(True),
      bunchSpacing = cms.int32(0),
      doPrefitEB = cms.bool(False),
      doPrefitEE = cms.bool(False),
      prefitMaxChiSqEB = cms.double(25),
      prefitMaxChiSqEE = cms.double(10),
      dynamicPedestalsEB = cms.bool(False),
      dynamicPedestalsEE = cms.bool(False),
      mitigateBadSamplesEB = cms.bool(False),
      mitigateBadSamplesEE = cms.bool(False),
      gainSwitchUseMaxSampleEB = cms.bool(True),
      gainSwitchUseMaxSampleEE = cms.bool(False),
      selectiveBadSampleCriteriaEB = cms.bool(False),
      selectiveBadSampleCriteriaEE = cms.bool(False),
      addPedestalUncertaintyEB = cms.double(0),
      addPedestalUncertaintyEE = cms.double(0),
      simplifiedNoiseModelForGainSwitch = cms.bool(True),
      timealgo = cms.string('RatioMethod'),
      EBtimeFitParameters = cms.vdouble(
        -2.015452,
        3.130702,
        -12.3473,
        41.88921,
        -82.83944,
        91.01147,
        -50.35761,
        11.05621
      ),
      EEtimeFitParameters = cms.vdouble(
        -2.390548,
        3.553628,
        -17.62341,
        67.67538,
        -133.213,
        140.7432,
        -75.41106,
        16.20277
      ),
      EBamplitudeFitParameters = cms.vdouble(
        1.138,
        1.652
      ),
      EEamplitudeFitParameters = cms.vdouble(
        1.89,
        1.4
      ),
      timeCalibTag = cms.ESInputTag('', ''),
      timeOffsetTag = cms.ESInputTag('', ''),
      EBtimeFitLimits_Lower = cms.double(0.2),
      EBtimeFitLimits_Upper = cms.double(1.4),
      EEtimeFitLimits_Lower = cms.double(0.2),
      EEtimeFitLimits_Upper = cms.double(1.4),
      EBtimeConstantTerm = cms.double(0.6),
      EEtimeConstantTerm = cms.double(1),
      EBtimeNconst = cms.double(28.5),
      EEtimeNconst = cms.double(31.8),
      outOfTimeThresholdGain12pEB = cms.double(5),
      outOfTimeThresholdGain12mEB = cms.double(5),
      outOfTimeThresholdGain61pEB = cms.double(5),
      outOfTimeThresholdGain61mEB = cms.double(5),
      outOfTimeThresholdGain12pEE = cms.double(1000),
      outOfTimeThresholdGain12mEE = cms.double(1000),
      outOfTimeThresholdGain61pEE = cms.double(1000),
      outOfTimeThresholdGain61mEE = cms.double(1000),
      amplitudeThresholdEB = cms.double(10),
      amplitudeThresholdEE = cms.double(10),
      crossCorrelationUseSlewCorrectionEB = cms.bool(True),
      crossCorrelationUseSlewCorrectionEE = cms.bool(False),
      crossCorrelationStartTime = cms.double(-25),
      crossCorrelationStopTime = cms.double(25),
      crossCorrelationTargetTimePrecision = cms.double(0.01),
      crossCorrelationTargetTimePrecisionForDelayedPulses = cms.double(0.05),
      crossCorrelationTimeShiftWrtRations = cms.double(0),
      crossCorrelationMinTimeToBeLateMin = cms.double(2),
      crossCorrelationMinTimeToBeLateMax = cms.double(5)
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
