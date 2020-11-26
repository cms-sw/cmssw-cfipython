import FWCore.ParameterSet.Config as cms

primaryVertexValidation = cms.EDAnalyzer('PrimaryVertexValidation',
  compressionSettings = cms.untracked.int32(-1),
  storeNtuple = cms.bool(False),
  isLightNtuple = cms.bool(True),
  useTracksFromRecoVtx = cms.bool(False),
  vertexZMax = cms.untracked.double(99),
  intLumi = cms.untracked.double(0),
  askFirstLayerHit = cms.bool(False),
  doBPix = cms.untracked.bool(True),
  doFPix = cms.untracked.bool(True),
  probePt = cms.untracked.double(0),
  probeP = cms.untracked.double(0),
  probeEta = cms.untracked.double(2.4),
  probeNHits = cms.untracked.double(0),
  numberOfBins = cms.untracked.int32(24),
  minPt = cms.untracked.double(1),
  maxPt = cms.untracked.double(20),
  Debug = cms.bool(False),
  runControl = cms.untracked.bool(False),
  forceBeamSpot = cms.untracked.bool(False),
  runControlNumber = cms.untracked.vuint32(0),
  TrackCollectionTag = cms.InputTag('ALCARECOTkAlMinBias'),
  VertexCollectionTag = cms.InputTag('offlinePrimaryVertices'),
  BeamSpotTag = cms.InputTag('offlineBeamSpot'),
  TkFilterParameters = cms.PSet(
    maxNormalizedChi2 = cms.double(5),
    minPt = cms.double(0),
    algorithm = cms.string('filter'),
    maxEta = cms.double(5),
    maxD0Significance = cms.double(5),
    maxD0Error = cms.double(1),
    maxDzError = cms.double(1),
    trackQuality = cms.string('any'),
    minPixelLayersWithHits = cms.int32(2),
    minSiliconLayersWithHits = cms.int32(5),
    numTracksThreshold = cms.int32(0)
  ),
  TkClusParameters = cms.PSet(
    TkDAClusParameters = cms.PSet(
      verbose = cms.untracked.bool(False),
      zdumpcenter = cms.untracked.double(0),
      zdumpwidth = cms.untracked.double(20),
      use_vdt = cms.untracked.bool(False),
      d0CutOff = cms.double(3),
      Tmin = cms.double(2),
      delta_lowT = cms.double(0.001),
      zmerge = cms.double(0.01),
      dzCutOff = cms.double(3),
      Tpurge = cms.double(2),
      convergence_mode = cms.int32(0),
      delta_highT = cms.double(0.01),
      Tstop = cms.double(0.5),
      coolingFactor = cms.double(0.6),
      vertexSize = cms.double(0.006),
      uniquetrkweight = cms.double(0.8),
      zrange = cms.double(4),
      tmerge = cms.double(0.01),
      dtCutOff = cms.double(4),
      t0Max = cms.double(1),
      vertexSizeTime = cms.double(0.008)
    ),
    TkGapClusParameters = cms.PSet(
      zSeparation = cms.double(1)
    ),
    algorithm = cms.string('DA_vect')
  ),
  mightGet = cms.optional.untracked.vstring
)
