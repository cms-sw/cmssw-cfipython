import FWCore.ParameterSet.Config as cms

primaryVertexProducer = cms.EDProducer('PrimaryVertexProducer',
  vertexCollections = cms.VPSet(
    cms.PSet(
      algorithm = cms.string('AdaptiveVertexFitter'),
      chi2cutoff = cms.double(2.5),
      label = cms.string(''),
      maxDistanceToBeam = cms.double(1),
      minNdof = cms.double(0),
      useBeamConstraint = cms.bool(False)
    ),
    cms.PSet(
      algorithm = cms.string('AdaptiveVertexFitter'),
      chi2cutoff = cms.double(2.5),
      label = cms.string('WithBS'),
      maxDistanceToBeam = cms.double(1),
      minNdof = cms.double(2),
      useBeamConstraint = cms.bool(True)
    )
  ),
  verbose = cms.untracked.bool(False),
  TkFilterParameters = cms.PSet(
    maxNormalizedChi2 = cms.double(10),
    minPt = cms.double(0),
    algorithm = cms.string('filter'),
    maxEta = cms.double(2.4),
    maxD0Significance = cms.double(4),
    maxD0Error = cms.double(1),
    maxDzError = cms.double(1),
    trackQuality = cms.string('any'),
    minPixelLayersWithHits = cms.int32(2),
    minSiliconLayersWithHits = cms.int32(5),
    numTracksThreshold = cms.int32(0)
  ),
  beamSpotLabel = cms.InputTag('offlineBeamSpot'),
  TrackLabel = cms.InputTag('generalTracks'),
  TrackTimeResosLabel = cms.InputTag('dummy_default'),
  TrackTimesLabel = cms.InputTag('dummy_default'),
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
