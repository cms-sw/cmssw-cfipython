import FWCore.ParameterSet.Config as cms

def PFRecoTauDiscriminationByNProngs(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauDiscriminationByNProngs',
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
    Prediscriminants = cms.PSet(
      BooleanOperator = cms.string('and')
    ),
    BooleanOutput = cms.bool(True),
    PFTauProducer = cms.InputTag('combinatoricRecoTaus'),
    MinN = cms.uint32(1),
    MaxN = cms.uint32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
