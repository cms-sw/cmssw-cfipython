import FWCore.ParameterSet.Config as cms

def PrimaryVertexProducer(**kwargs):
  mod = cms.EDProducer('PrimaryVertexProducer',
    vertexCollections = cms.VPSet(
      cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string(''),
        maxDistanceToBeam = cms.double(1),
        minNdof = cms.double(0),
        mintrkweight = cms.double(0),
        useBeamConstraint = cms.bool(False),
        zcutoff = cms.double(1),
        vertexTimeParameters = cms.PSet(
          algorithm = cms.string('')
        )
      ),
      cms.PSet(
        algorithm = cms.string('AdaptiveVertexFitter'),
        chi2cutoff = cms.double(2.5),
        label = cms.string('WithBS'),
        maxDistanceToBeam = cms.double(1),
        minNdof = cms.double(2),
        mintrkweight = cms.double(0),
        useBeamConstraint = cms.bool(True),
        zcutoff = cms.double(1),
        vertexTimeParameters = cms.PSet(
          algorithm = cms.string('')
        )
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
      minValidStripHits = cms.int32(0),
      numTracksThreshold = cms.int32(0),
      maxNumTracksThreshold = cms.int32(2147483647),
      minPtTight = cms.double(0)
    ),
    beamSpotLabel = cms.InputTag('offlineBeamSpot'),
    TrackLabel = cms.InputTag('generalTracks'),
    TrackTimeResosLabel = cms.InputTag('dummy_default'),
    TrackTimesLabel = cms.InputTag('dummy_default'),
    trackMTDTimeQualityVMapTag = cms.InputTag('mtdTrackQualityMVA', 'mtdQualMVA'),
    TkClusParameters = cms.PSet(
      algorithm = cms.string('DA_vect'),
      TkDAClusParameters = cms.PSet(
        zdumpcenter = cms.untracked.double(0),
        zdumpwidth = cms.untracked.double(20),
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
        uniquetrkminp = cms.double(0),
        zrange = cms.double(4),
        runInBlocks = cms.bool(False),
        block_size = cms.uint32(10000),
        overlap_frac = cms.double(0)
      )
    ),
    isRecoveryIteration = cms.bool(False),
    recoveryVtxCollection = cms.InputTag(''),
    useMVACut = cms.bool(False),
    minTrackTimeQuality = cms.double(0.8),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
