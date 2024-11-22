import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationByIsolation(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationByIsolation',
    storeRawFootprintCorrection = cms.bool(False),
    PFTauProducer = cms.InputTag('pfRecoTauProducer'),
    storeRawOccupancy = cms.bool(False),
    maximumSumPtCut = cms.double(6),
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
    maxAbsPhotonSumPt_outsideSignalCone = cms.double(1000000000),
    vertexSrc = cms.InputTag('offlinePrimaryVertices'),
    applySumPtCut = cms.bool(False),
    rhoConeSize = cms.double(0.5),
    ApplyDiscriminationByTrackerIsolation = cms.bool(True),
    storeRawPhotonSumPt_outsideSignalCone = cms.bool(False),
    rhoProducer = cms.InputTag('fixedGridRhoFastjetAll'),
    enableHGCalWorkaround = cms.bool(False),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
