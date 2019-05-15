import FWCore.ParameterSet.Config as cms

ecalRecHit = cms.EDProducer('EcalRecHitProducer',
  recoverEEVFE = cms.bool(False),
  EErechitCollection = cms.string('EcalRecHitsEE'),
  recoverEBIsolatedChannels = cms.bool(False),
  recoverEBVFE = cms.bool(False),
  laserCorrection = cms.bool(True),
  EBLaserMIN = cms.double(0.5),
  killDeadChannels = cms.bool(True),
  dbStatusToBeExcludedEB = cms.vint32(
    14,
    78,
    142
  ),
  EEuncalibRecHitCollection = cms.InputTag('ecalMultiFitUncalibRecHit', 'EcalUncalibRecHitsEE'),
  dbStatusToBeExcludedEE = cms.vint32(
    14,
    78,
    142
  ),
  EELaserMIN = cms.double(0.5),
  ebFEToBeRecovered = cms.InputTag('ecalDetIdToBeRecovered', 'ebFE'),
  cleaningConfig = cms.PSet(
    e6e2thresh = cms.double(0.04),
    tightenCrack_e6e2_double = cms.double(3),
    e4e1Threshold_endcap = cms.double(0.3),
    tightenCrack_e4e1_single = cms.double(3),
    tightenCrack_e1_double = cms.double(2),
    cThreshold_barrel = cms.double(4),
    e4e1Threshold_barrel = cms.double(0.08),
    tightenCrack_e1_single = cms.double(2),
    e4e1_b_barrel = cms.double(-0.024),
    e4e1_a_barrel = cms.double(0.04),
    ignoreOutOfTimeThresh = cms.double(1000000000),
    cThreshold_endcap = cms.double(15),
    e4e1_b_endcap = cms.double(-0.0125),
    e4e1_a_endcap = cms.double(0.02),
    cThreshold_double = cms.double(10)
  ),
  logWarningEtThreshold_EE_FE = cms.double(50),
  eeDetIdToBeRecovered = cms.InputTag('ecalDetIdToBeRecovered', 'eeDetId'),
  recoverEBFE = cms.bool(True),
  eeFEToBeRecovered = cms.InputTag('ecalDetIdToBeRecovered', 'eeFE'),
  ebDetIdToBeRecovered = cms.InputTag('ecalDetIdToBeRecovered', 'ebDetId'),
  singleChannelRecoveryThreshold = cms.double(8),
  ChannelStatusToBeExcluded = cms.vstring(
    'kNoisy',
    'kNNoisy',
    'kFixedG6',
    'kFixedG1',
    'kFixedG0',
    'kNonRespondingIsolated',
    'kDeadVFE',
    'kDeadFE',
    'kNoDataNoTP'
  ),
  EBrechitCollection = cms.string('EcalRecHitsEB'),
  triggerPrimitiveDigiCollection = cms.InputTag('ecalDigis', 'EcalTriggerPrimitives'),
  recoverEEFE = cms.bool(True),
  singleChannelRecoveryMethod = cms.string('NeuralNetworks'),
  EBLaserMAX = cms.double(3),
  flagsMapDBReco = cms.PSet(
    kGood = cms.vstring(
      'kOk',
      'kDAC',
      'kNoLaser',
      'kNoisy'
    ),
    kNeighboursRecovered = cms.vstring(
      'kFixedG0',
      'kNonRespondingIsolated',
      'kDeadVFE'
    ),
    kDead = cms.vstring('kNoDataNoTP'),
    kNoisy = cms.vstring(
      'kNNoisy',
      'kFixedG6',
      'kFixedG1'
    ),
    kTowerRecovered = cms.vstring('kDeadFE')
  ),
  EBuncalibRecHitCollection = cms.InputTag('ecalMultiFitUncalibRecHit', 'EcalUncalibRecHitsEB'),
  algoRecover = cms.string('EcalRecHitWorkerRecover'),
  algo = cms.string('EcalRecHitWorkerSimple'),
  EELaserMAX = cms.double(8),
  logWarningEtThreshold_EB_FE = cms.double(50),
  recoverEEIsolatedChannels = cms.bool(False),
  skipTimeCalib = cms.bool(False)
)
