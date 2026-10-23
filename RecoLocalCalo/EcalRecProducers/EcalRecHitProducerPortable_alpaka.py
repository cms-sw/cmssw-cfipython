import FWCore.ParameterSet.Config as cms

def EcalRecHitProducerPortable_alpaka(*args, **kwargs):
  mod = cms.EDProducer('EcalRecHitProducerPortable@alpaka',
    uncalibrecHitsInLabelEB = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEB'),
    recHitsLabelEB = cms.string('EcalRecHitsEB'),
    killDeadChannels = cms.bool(True),
    recoverEBIsolatedChannels = cms.bool(False),
    recoverEBVFE = cms.bool(False),
    recoverEBFE = cms.bool(True),
    EBLaserMIN = cms.double(0.5),
    EBLaserMAX = cms.double(3),
    isPhase2 = cms.bool(False),
    uncalibrecHitsInLabelEE = cms.InputTag('ecalMultiFitUncalibRecHitPortable', 'EcalUncalibRecHitsEE'),
    recHitsLabelEE = cms.string('EcalRecHitsEE'),
    recoverEEIsolatedChannels = cms.bool(False),
    recoverEEVFE = cms.bool(False),
    recoverEEFE = cms.bool(True),
    EELaserMIN = cms.double(0.5),
    EELaserMAX = cms.double(8),
    ChannelStatusToBeExcluded = cms.vstring(
      'kDAC',
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
