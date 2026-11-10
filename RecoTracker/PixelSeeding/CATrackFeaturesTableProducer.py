import FWCore.ParameterSet.Config as cms

def CATrackFeaturesTableProducer(*args, **kwargs):
  mod = cms.EDProducer('CATrackFeaturesTableProducer',
    tableName = cms.string('TrkPromptCA'),
    trackSrc = cms.InputTag('pixelTracksAlpaka'),
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    otRecHitsSoASrc = cms.InputTag('caOTRecHitsSoA'),
    emitHitTruth = cms.bool(False),
    hitTableName = cms.string('TrkPromptCAHit'),
    minSharedForOwnTP = cms.int32(3),
    vectorHitsSrc = cms.InputTag('phase2OTVectorHitsSoA'),
    otRecHitSrc = cms.InputTag('siPhase2RecHits'),
    trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth'),
    TP_signalOnly = cms.bool(False),
    TP_chargedOnly = cms.bool(True),
    TP_minPt = cms.double(0),
    TP_maxEta = cms.double(4.5),
    TP_maxTip = cms.double(60),
    TP_maxVtxZ = cms.double(60),
    hitAssociatorConfig = cms.PSet(
      associatePixel = cms.bool(True),
      associateStrip = cms.bool(True),
      usePhase2Tracker = cms.bool(True),
      associateRecoTracks = cms.bool(False),
      associateHitbySimTrack = cms.bool(False),
      phase2TrackerSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Tracker'),
      pixelSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Pixel'),
      stripSimLinkSrc = cms.InputTag('simSiStripDigis'),
      ROUList = cms.vstring(
        'TrackerHitsPixelBarrelLowTof',
        'TrackerHitsPixelBarrelHighTof',
        'TrackerHitsPixelEndcapLowTof',
        'TrackerHitsPixelEndcapHighTof',
        'TrackerHitsTIBLowTof',
        'TrackerHitsTIBHighTof',
        'TrackerHitsTIDLowTof',
        'TrackerHitsTIDHighTof',
        'TrackerHitsTOBLowTof',
        'TrackerHitsTOBHighTof',
        'TrackerHitsTECLowTof',
        'TrackerHitsTECHighTof'
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
