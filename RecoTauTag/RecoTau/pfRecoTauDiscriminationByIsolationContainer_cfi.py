import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByIsolationContainer = cms.EDProducer('PFRecoTauDiscriminationByIsolationContainer',
  PFTauProducer = cms.InputTag('pfRecoTauProducer'),
  qualityCuts = cms.PSet(
    signalQualityCuts = cms.PSet(
      minTrackPt = cms.double(0.5),
      maxTrackChi2 = cms.double(100),
      maxTransverseImpactParameter = cms.double(0.1),
      maxDeltaZ = cms.double(0.4),
      maxDeltaZToLeadTrack = cms.double(-1),
      minTrackVertexWeight = cms.double(-1),
      minTrackPixelHits = cms.uint32(0),
      minTrackHits = cms.uint32(3),
      minGammaEt = cms.double(1),
      useTracksInsteadOfPFHadrons = cms.optional.bool,
      minNeutralHadronEt = cms.double(30)
    ),
    isolationQualityCuts = cms.PSet(
      minTrackPt = cms.double(1),
      maxTrackChi2 = cms.double(100),
      maxTransverseImpactParameter = cms.double(0.03),
      maxDeltaZ = cms.double(0.2),
      maxDeltaZToLeadTrack = cms.double(-1),
      minTrackVertexWeight = cms.double(-1),
      minTrackPixelHits = cms.uint32(0),
      minTrackHits = cms.uint32(8),
      minGammaEt = cms.double(1.5),
      useTracksInsteadOfPFHadrons = cms.optional.bool
    ),
    vxAssocQualityCuts = cms.PSet(
      minTrackPt = cms.double(0.5),
      maxTrackChi2 = cms.double(100),
      maxTransverseImpactParameter = cms.double(0.1),
      minTrackVertexWeight = cms.double(-1),
      minTrackPixelHits = cms.uint32(0),
      minTrackHits = cms.uint32(3),
      minGammaEt = cms.double(1),
      useTracksInsteadOfPFHadrons = cms.optional.bool
    ),
    primaryVertexSrc = cms.InputTag('offlinePrimaryVertices'),
    pvFindingAlgo = cms.string('closestInDeltaZ'),
    vertexTrackFiltering = cms.bool(False),
    recoverLeadingTrk = cms.bool(False),
    leadingTrkOrPFCandOption = cms.string('leadPFCand')
  ),
  minTauPtForNoIso = cms.double(-99),
  vertexSrc = cms.InputTag('offlinePrimaryVertices'),
  rhoConeSize = cms.double(0.5),
  rhoProducer = cms.InputTag('fixedGridRhoFastjetAll'),
  footprintCorrections = cms.VPSet(
  ),
  deltaBetaFactor = cms.string('0.38'),
  applyFootprintCorrection = cms.bool(False),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
      cut = cms.double(0.5),
      Producer = cms.InputTag('pfRecoTauDiscriminationByLeadingTrackFinding')
    ),
    decayMode = cms.PSet(
      cut = cms.double(0.5),
      Producer = cms.InputTag('hpsPFTauDiscriminationByDecayModeFindingNewDMs')
    ),
    preIso = cms.PSet(
      cut = cms.double(0.5),
      Producer = cms.InputTag('hpsPFTauDiscriminationByLooseChargedIsolation')
    )
  ),
  verbosity = cms.int32(0),
  deltaBetaPUTrackPtCutOverride = cms.bool(False),
  applyRhoCorrection = cms.bool(False),
  WeightECALIsolation = cms.double(1),
  rhoUEOffsetCorrection = cms.double(1),
  deltaBetaPUTrackPtCutOverride_val = cms.double(-1.5),
  isoConeSizeForDeltaBeta = cms.double(0.5),
  customOuterCone = cms.double(-1),
  particleFlowSrc = cms.InputTag('particleFlow'),
  IDdefinitions = cms.VPSet(
  ),
  IDWPdefinitions = cms.VPSet(
  ),
  mightGet = cms.optional.untracked.vstring
)
