import FWCore.ParameterSet.Config as cms

def HitTruthTableProducer(*args, **kwargs):
  mod = cms.EDProducer('HitTruthTableProducer',
    tableName = cms.string('HitTruth'),
    pixelRecHitSoASrc = cms.InputTag('siPixelRecHitsPreSplittingAlpaka'),
    otRecHitsSoASrc = cms.InputTag('caOTRecHitsSoA'),
    vectorHitsSrc = cms.InputTag('phase2OTVectorHitsSoA'),
    otRecHitSrc = cms.InputTag('siPhase2RecHits'),
    pixelRecHitSrc = cms.InputTag('siPixelRecHitsPreSplitting'),
    trackingParticleSrc = cms.InputTag('mix', 'MergedTrackTruth'),
    emitHitFeatures = cms.bool(False),
    otTableName = cms.string('HitTruthOT'),
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
