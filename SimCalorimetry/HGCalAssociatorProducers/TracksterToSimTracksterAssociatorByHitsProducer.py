import FWCore.ParameterSet.Config as cms

def TracksterToSimTracksterAssociatorByHitsProducer(*args, **kwargs):
  mod = cms.EDProducer('TracksterToSimTracksterAssociatorByHitsProducer',
    tracksters = cms.InputTag('ticlTrackstersMerge'),
    simTracksters = cms.InputTag('ticlSimTracksters'),
    simTrackstersFromCP = cms.InputTag('ticlSimTracksters', 'fromCPs'),
    hitToTracksterMap = cms.InputTag('hitToTracksterAssociator', 'hitToTracksterMap'),
    hitToSimTracksterMap = cms.InputTag('allHitToTracksterAssociations', 'hitToticlSimTracksters'),
    hitToSimTracksterFromCPMap = cms.InputTag('allHitToTracksterAssociations', 'hitToticlSimTrackstersfromCPs'),
    hitToSimClusterMap = cms.InputTag('hitToSimClusterCaloParticleAssociator', 'hitToSimClusterMap'),
    hitToCaloParticleMap = cms.InputTag('hitToSimClusterCaloParticleAssociator', 'hitToCaloParticleMap'),
    tracksterToHitMap = cms.InputTag('hitToTrackstersAssociationPR', 'tracksterToHitMap'),
    simTracksterToHitMap = cms.InputTag('allHitToTracksterAssociations', 'ticlSimTrackstersToHit'),
    simTracksterFromCPToHitMap = cms.InputTag('allHitToTracksterAssociations', 'ticlSimTrackstersfromCPsToHit'),
    caloParticles = cms.InputTag('mix', 'MergedCaloTruth'),
    hits = cms.VInputTag(
      'HGCalRecHit:HGCEERecHits',
      'HGCalRecHit:HGCHEFRecHits',
      'HGCalRecHit:HGCHEBRecHits'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
