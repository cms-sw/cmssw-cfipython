import FWCore.ParameterSet.Config as cms

def Phase2OTValidateVectorHitsSoA(*args, **kwargs):
  mod = cms.EDProducer('Phase2OTValidateVectorHitsSoA',
    TopFolderName = cms.string('HLT/TrackerPhase2OTVectorHitsSoAV'),
    vectorHitsSrc = cms.InputTag('phase2OTVectorHitsSoA'),
    otRecHitsSrc = cms.InputTag('caOTRecHitsSoA'),
    recHitSrc = cms.InputTag('siPhase2RecHits'),
    trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth'),
    TP_minPt = cms.double(0.75),
    TP_maxEta = cms.double(4.2),
    TP_maxVtxZ = cms.double(60),
    TP_maxD0 = cms.double(5),
    TP_maxLxy = cms.double(60),
    TP_minNLayers = cms.int32(4),
    clusterTPAssociationSrc = cms.InputTag('tpClusterProducer'),
    beamSpot = cms.InputTag('offlineBeamSpot'),
    simHitSrc = cms.VInputTag(
      'g4SimHits:TrackerHitsPixelBarrelLowTof',
      'g4SimHits:TrackerHitsPixelBarrelHighTof',
      'g4SimHits:TrackerHitsPixelEndcapLowTof',
      'g4SimHits:TrackerHitsPixelEndcapHighTof'
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
