import FWCore.ParameterSet.Config as cms

def alpaka_serial_sync_EcalUncalibRecHitProducerPortable(*args, **kwargs):
  mod = cms.EDProducer('alpaka_serial_sync::EcalUncalibRecHitProducerPortable',
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
    kernelMinimizeThreads = cms.untracked.vuint32(
      32,
      1,
      1
    ),
    shouldRunTimingComputation = cms.bool(True),
    mightGet = cms.optional.untracked.vstring,
    alpaka = cms.untracked.PSet(
      backend = cms.untracked.string('')
    )
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
