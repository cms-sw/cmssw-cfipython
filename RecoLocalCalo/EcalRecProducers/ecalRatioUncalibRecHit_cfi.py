import FWCore.ParameterSet.Config as cms

ecalRatioUncalibRecHit = cms.EDProducer('EcalUncalibRecHitProducer',
  EBdigiCollection = cms.InputTag('ecalDigis', 'ebDigis'),
  EEhitCollection = cms.string('EcalUncalibRecHitsEE'),
  EEdigiCollection = cms.InputTag('ecalDigis', 'eeDigis'),
  EBhitCollection = cms.string('EcalUncalibRecHitsEB'),
  algo = cms.string('EcalUncalibRecHitWorkerRatio'),
  algoPSet = cms.PSet(
    EEtimeFitLimits_Upper = cms.double(1.4),
    EEtimeConstantTerm = cms.double(0.18),
    EBtimeFitLimits_Lower = cms.double(0.2),
    EBtimeConstantTerm = cms.double(0.26),
    EEtimeFitLimits_Lower = cms.double(0.2),
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
    EEamplitudeFitParameters = cms.vdouble(
      1.89,
      1.4
    ),
    EBtimeFitLimits_Upper = cms.double(1.4),
    EBamplitudeFitParameters = cms.vdouble(
      1.138,
      1.652
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
    )
  )
)
