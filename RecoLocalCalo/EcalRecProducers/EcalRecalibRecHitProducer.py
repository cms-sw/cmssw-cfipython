import FWCore.ParameterSet.Config as cms

def EcalRecalibRecHitProducer(*args, **kwargs):
  mod = cms.EDProducer('EcalRecalibRecHitProducer',
    EBRecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEB'),
    EERecHitCollection = cms.InputTag('ecalRecHit', 'EcalRecHitsEE'),
    EBRecalibRecHitCollection = cms.string('EcalRecHitsEB'),
    EERecalibRecHitCollection = cms.string('EcalRecHitsEE'),
    doEnergyScale = cms.bool(False),
    doIntercalib = cms.bool(False),
    doLaserCorrections = cms.bool(False),
    doEnergyScaleInverse = cms.bool(False),
    doIntercalibInverse = cms.bool(False),
    doLaserCorrectionsInverse = cms.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
