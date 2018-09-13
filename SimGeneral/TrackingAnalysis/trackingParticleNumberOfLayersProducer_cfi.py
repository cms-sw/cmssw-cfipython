import FWCore.ParameterSet.Config as cms

trackingParticleNumberOfLayersProducer = cms.EDProducer('TrackingParticleNumberOfLayersProducer',
  trackingParticles = cms.InputTag('mix', 'MergedTrackTruth'),
  simHits = cms.VInputTag(
    'g4SimHits:TrackerHitsPixelBarrelHighTof',
    'g4SimHits:TrackerHitsPixelBarrelLowTof',
    'g4SimHits:TrackerHitsPixelEndcapHighTof',
    'g4SimHits:TrackerHitsPixelEndcapLowTof',
    'g4SimHits:TrackerHitsTECHighTof',
    'g4SimHits:TrackerHitsTECLowTof',
    'g4SimHits:TrackerHitsTIBHighTof',
    'g4SimHits:TrackerHitsTIBLowTof',
    'g4SimHits:TrackerHitsTIDHighTof',
    'g4SimHits:TrackerHitsTIDLowTof',
    'g4SimHits:TrackerHitsTOBHighTof',
    'g4SimHits:TrackerHitsTOBLowTof'
  )
)
