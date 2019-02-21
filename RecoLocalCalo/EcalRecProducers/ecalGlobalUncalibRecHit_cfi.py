import FWCore.ParameterSet.Config as cms

ecalGlobalUncalibRecHit = cms.EDProducer('EcalUncalibRecHitProducer',
  EBdigiCollection = cms.InputTag('ecalDigis', 'ebDigis'),
  EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
  EEdigiCollection = cms.InputTag('ecalDigis', 'eeDigis'),
  EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
  algo = cms.string('EcalUncalibRecHitWorkerGlobal'),
  algoPSet = cms.PSet(
    eePulseShape = cms.vdouble(
      5.2e-05,
      -5.26e-05,
      6.66e-05,
      0.1168,
      0.7575,
      1,
      0.8876,
      0.6732,
      0.4741,
      0.3194
    ),
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
    outOfTimeThresholdGain61pEB = cms.double(5),
    amplitudeThresholdEE = cms.double(10),
    EBtimeConstantTerm = cms.double(0.6),
    outOfTimeThresholdGain61pEE = cms.double(1000),
    ebSpikeThreshold = cms.double(1.042),
    EBtimeNconst = cms.double(28.5),
    kPoorRecoFlagEB = cms.bool(True),
    ebPulseShape = cms.vdouble(
      5.2e-05,
      -5.26e-05,
      6.66e-05,
      0.1168,
      0.7575,
      1,
      0.8876,
      0.6732,
      0.4741,
      0.3194
    ),
    EBtimeFitLimits_Lower = cms.double(0.2),
    kPoorRecoFlagEE = cms.bool(False),
    chi2ThreshEB_ = cms.double(36),
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
    outOfTimeThresholdGain61mEE = cms.double(1000),
    EEchi2Parameters = cms.vdouble(
      2.122,
      0.022,
      2.122,
      0.022
    ),
    outOfTimeThresholdGain12mEE = cms.double(1000),
    outOfTimeThresholdGain12mEB = cms.double(5),
    EEtimeFitLimits_Upper = cms.double(1.4),
    EEtimeFitLimits_Lower = cms.double(0.2),
    EEamplitudeFitParameters = cms.vdouble(
      1.89,
      1.4
    ),
    EBamplitudeFitParameters = cms.vdouble(
      1.138,
      1.652
    ),
    amplitudeThresholdEB = cms.double(10),
    outOfTimeThresholdGain12pEE = cms.double(1000),
    outOfTimeThresholdGain12pEB = cms.double(5),
    EEtimeNconst = cms.double(31.8),
    outOfTimeThresholdGain61mEB = cms.double(5),
    EBchi2Parameters = cms.vdouble(
      2.122,
      0.022,
      2.122,
      0.022
    ),
    EEtimeConstantTerm = cms.double(1),
    chi2ThreshEE_ = cms.double(95),
    EBtimeFitLimits_Upper = cms.double(1.4)
  )
)
