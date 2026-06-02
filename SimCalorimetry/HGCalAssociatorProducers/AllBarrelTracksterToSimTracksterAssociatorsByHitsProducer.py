import FWCore.ParameterSet.Config as cms

def AllBarrelTracksterToSimTracksterAssociatorsByHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('AllBarrelTracksterToSimTracksterAssociatorsByHitsProducer',
    allHitToTSAccoc = cms.string('allHitToTracksterAssociations'),
    tracksterCollections = cms.VInputTag(
      'ticlTrackstersCLUE3DHigh',
      'ticlTrackstersLinks'
    ),
    simTracksterCollections = cms.VInputTag(
      'ticlSimTracksters',
      'ticlSimTracksters:fromCPs'
    ),
    hitToSimClusterMap = cms.InputTag('hitToSimClusterCaloParticleAssociator', 'hitToSimClusterMap'),
    hitToCaloParticleMap = cms.InputTag('hitToSimClusterCaloParticleAssociator', 'hitToCaloParticleMap'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    hits = cms.InputTag('recHitMapProducer', 'RefProdVectorPFRecHitCollection'),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
