import FWCore.ParameterSet.Config as cms

pfRecoTauDiscriminationByNProngs = cms.EDProducer('PFRecoTauDiscriminationByNProngs',
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
      maxTransverseImpactParameter = cms.double(0.1)
    ),
    vxAssocQualityCuts = cms.PSet(
      minTrackPt = cms.double(0.5),
      minTrackVertexWeight = cms.double(-1),
      maxTrackChi2 = cms.double(100),
      minTrackPixelHits = cms.uint32(0),
      minGammaEt = cms.double(1),
      minTrackHits = cms.uint32(3),
      maxTransverseImpactParameter = cms.double(0.1)
    ),
    isolationQualityCuts = cms.PSet(
      maxDeltaZ = cms.double(0.2),
      minTrackPt = cms.double(1),
      minTrackVertexWeight = cms.double(-1),
      maxTrackChi2 = cms.double(100),
      minTrackPixelHits = cms.uint32(0),
      minGammaEt = cms.double(1.5),
      minTrackHits = cms.uint32(8),
      maxTransverseImpactParameter = cms.double(0.03)
    ),
    leadingTrkOrPFCandOption = cms.string('leadPFCand'),
    pvFindingAlgo = cms.string('closestInDeltaZ'),
    primaryVertexSrc = cms.InputTag('offlinePrimaryVertices'),
    vertexTrackFiltering = cms.bool(False),
    recoverLeadingTrk = cms.bool(False)
  ),
  Prediscriminants = cms.PSet(
    BooleanOperator = cms.string('and')
  ),
  BooleanOutput = cms.bool(True),
  PFTauProducer = cms.InputTag('combinatoricRecoTaus'),
  MinN = cms.uint32(1),
  MaxN = cms.uint32(0)
)
