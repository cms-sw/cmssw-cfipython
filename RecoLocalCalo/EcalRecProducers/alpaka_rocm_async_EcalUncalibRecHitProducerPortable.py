import FWCore.ParameterSet.Config as cms

def alpaka_rocm_async_EcalUncalibRecHitProducerPortable(*args, **kwargs):
  mod = cms.EDProducer('alpaka_rocm_async::EcalUncalibRecHitProducerPortable',
    digisLabelEB = cms.InputTag('ecalRawToDigiPortable', 'ebDigis'),
    digisLabelEE = cms.InputTag('ecalRawToDigiPortable', 'eeDigis'),
    recHitsLabelEB = cms.string('EcalUncalibRecHitsEB'),
    recHitsLabelEE = cms.string('EcalUncalibRecHitsEE'),
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
    kernelMinimizeThreads = cms.untracked.vuint32(
      32,
      1,
      1
    ),
    shouldRunTimingComputation = cms.bool(True),
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
