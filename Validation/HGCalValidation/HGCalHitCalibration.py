import FWCore.ParameterSet.Config as cms

def HGCalHitCalibration(*args, **kwargs):
  mod = cms.EDProducer('HGCalHitCalibration',
    debug = cms.int32(0),
    rawRecHits = cms.bool(True),
    folder = cms.string('HGCalHitCalibration'),
    detector = cms.string('all'),
    depletionFine = cms.int32(120),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    recHitsEE = cms.InputTag('HGCalRecHit', 'HGCEERecHits'),
    recHitsFH = cms.InputTag('HGCalRecHit', 'HGCHEFRecHits'),
    recHitsBH = cms.InputTag('HGCalRecHit', 'HGCHEBRecHits'),
    hgcalMultiClusters = cms.InputTag('particleFlowClusterHGCal'),
    electrons = cms.InputTag('ecalDrivenGsfElectronsHGC'),
    photons = cms.InputTag('photonsHGC'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
