import FWCore.ParameterSet.Config as cms

def HGCalHitCalibration(**kwargs):
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod