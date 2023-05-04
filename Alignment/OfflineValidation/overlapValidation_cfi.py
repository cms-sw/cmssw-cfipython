import FWCore.ParameterSet.Config as cms

overlapValidation = cms.EDAnalyzer('OverlapValidation',
  associatePixel = cms.bool(False),
  associateStrip = cms.bool(False),
  usePhase2Tracker = cms.bool(False),
  associateRecoTracks = cms.bool(False),
  associateHitbySimTrack = cms.bool(False),
  phase2TrackerSimLinkSrc = cms.InputTag('simSiPixelDigis', 'Tracker'),
  stripSimLinkSrc = cms.InputTag('simSiStripDigis'),
  pixelSimLinkSrc = cms.InputTag('simSiPixelDigis'),
  ROUList = cms.vstring(
    'TrackerHitsTIBLowTof',
    'TrackerHitsTIBHighTof',
    'TrackerHitsTOBLowTof',
    'TrackerHitsTOBHighTof'
  ),
  compressionSettings = cms.untracked.int32(-1),
  trajectories = cms.InputTag('FinalTrackRefitter'),
  barrelOnly = cms.bool(False),
  usePXB = cms.bool(True),
  usePXF = cms.bool(True),
  useTIB = cms.bool(True),
  useTOB = cms.bool(True),
  useTID = cms.bool(True),
  useTEC = cms.bool(True),
  mightGet = cms.optional.untracked.vstring
)
