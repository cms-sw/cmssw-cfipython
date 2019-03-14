import FWCore.ParameterSet.Config as cms

trackingParticleNumberOfLayersProducer = cms.EDProducer('TrackingParticleNumberOfLayersProducer',
  trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
  simHits = cms.VInputTag(
    'g4SimHits:TrackerHitsPixelBarrelLowTof',
    'g4SimHits:TrackerHitsPixelBarrelHighTof',
    'g4SimHits:TrackerHitsPixelEndcapLowTof',
    'g4SimHits:TrackerHitsPixelEndcapHighTof',
    'g4SimHits:TrackerHitsTIBLowTof',
    'g4SimHits:TrackerHitsTIBHighTof',
    'g4SimHits:TrackerHitsTIDLowTof',
    'g4SimHits:TrackerHitsTIDHighTof',
    'g4SimHits:TrackerHitsTOBLowTof',
    'g4SimHits:TrackerHitsTOBHighTof',
    'g4SimHits:TrackerHitsTECLowTof',
    'g4SimHits:TrackerHitsTECHighTof'
  )
)
