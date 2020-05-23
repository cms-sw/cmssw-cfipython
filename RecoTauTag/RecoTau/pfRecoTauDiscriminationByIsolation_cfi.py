import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByIsolation = cms.EDProducer('PFRecoTauDiscriminationByIsolation',
  storeRawFootprintCorrection = cms.bool(False),
  PFTauProducer = cms.InputTag('pfRecoTauProducer'),
  storeRawOccupancy = cms.bool(False),
  maximumSumPtCut = cms.double(6),
  qualityCuts = cms.PSet(
    signalQualityCuts = cms.PSet(
      maxDeltaZ = cms.double(0.4),
      minTrackPt = cms.double(0.5),
      minTrackVertexWeight = cms.double(-1),
      maxTrackChi2 = cms.double(100),
      minTrackPixelHits = cms.uint32(0),
      minGammaEt = cms.double(1),
      minTrackHits = cms.uint32(3),
      minNeutralHadronEt = cms.double(30),
      maxTransverseImpactParameter = cms.double(0.1),
      useTracksInsteadOfPFHadrons = cms.optional.bool
    ),
    vxAssocQualityCuts = cms.PSet(
      minTrackPt = cms.double(0.5),
      minTrackVertexWeight = cms.double(-1),
      maxTrackChi2 = cms.double(100),
      minTrackPixelHits = cms.uint32(0),
      minGammaEt = cms.double(1),
      minTrackHits = cms.uint32(3),
      maxTransverseImpactParameter = cms.double(0.1),
      useTracksInsteadOfPFHadrons = cms.optional.bool
    ),
    isolationQualityCuts = cms.PSet(
      maxDeltaZ = cms.double(0.2),
      minTrackPt = cms.double(1),
      minTrackVertexWeight = cms.double(-1),
      maxTrackChi2 = cms.double(100),
      minTrackPixelHits = cms.uint32(0),
      minGammaEt = cms.double(1.5),
      minTrackHits = cms.uint32(8),
      maxTransverseImpactParameter = cms.double(0.03),
      useTracksInsteadOfPFHadrons = cms.optional.bool
    ),
    leadingTrkOrPFCandOption = cms.string('leadPFCand'),
    pvFindingAlgo = cms.string('closestInDeltaZ'),
    primaryVertexSrc = cms.InputTag('offlinePrimaryVertices'),
    vertexTrackFiltering = cms.bool(False),
    recoverLeadingTrk = cms.bool(False)
  ),
  minTauPtForNoIso = cms.double(-99),
  maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000),
  vertexSrc = cms.InputTag('offlinePrimaryVertices'),
  applySumPtCut = cms.bool(False),
  rhoConeSize = cms.double(0.5),
  ApplyDiscriminationByTrackerIsolation = cms.bool(True),
  storeRawPhotonSumPt_outsideSignalCone = cms.bool(False),
  rhoProducer = cms.InputTag('fixedGridRhoFastjetAll'),
  footprintCorrections = cms.VPSet(
  ),
  deltaBetaFactor = cms.string('0.38'),
  applyFootprintCorrection = cms.bool(False),
  UseAllPFCandsForWeights = cms.bool(False),
  relativeSumPtCut = cms.double(0),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and'),
    leadTrack = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    ),
    decayMode = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    ),
    preIso = cms.PSet(
      cut = cms.required.double,
      Producer = cms.required.InputTag
    )
  ),
  maximumOccupancy = cms.uint32(0),
  verbosity = cms.int32(0),
  applyOccupancyCut = cms.bool(True),
  applyDeltaBetaCorrection = cms.bool(False),
  applyRelativeSumPtCut = cms.bool(False),
  storeRawPUsumPt = cms.bool(False),
  applyPhotonPtSumOutsideSignalConeCut = cms.bool(False),
  deltaBetaPUTrackPtCutOverride = cms.bool(False),
  ApplyDiscriminationByWeightedECALIsolation = cms.bool(False),
  storeRawSumPt = cms.bool(False),
  ApplyDiscriminationByECALIsolation = cms.bool(True),
  applyRhoCorrection = cms.bool(False),
  WeightECALIsolation = cms.double(1),
  rhoUEOffsetCorrection = cms.double(1),
  maxRelPhotonSumPt_outsideSignalCone = cms.double(0.1),
  deltaBetaPUTrackPtCutOverride_val = cms.double(-1.5),
  isoConeSizeForDeltaBeta = cms.double(0.5),
  relativeSumPtOffset = cms.double(0),
  customOuterCone = cms.double(-1),
  particleFlowSrc = cms.InputTag('particleFlow'),
  mightGet = cms.optional.untracked.vstring
)
