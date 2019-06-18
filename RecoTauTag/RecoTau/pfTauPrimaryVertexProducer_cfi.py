import FWCore.ParameterSet.Config as cms

pfTauPrimaryVertexProducer = cms.EDProducer('PFTauPrimaryVertexProducer',
  discriminators = cms.required.VPSet,
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
  cut = cms.string('pt > 18.0 & abs(eta)<2.3'),
  Algorithm = cms.int32(0),
  RemoveElectronTracks = cms.bool(False),
  RemoveMuonTracks = cms.bool(False),
  useBeamSpot = cms.bool(True),
  useSelectedTaus = cms.bool(False),
  beamSpot = cms.InputTag('offlineBeamSpot'),
  ElectronTag = cms.InputTag('MyElectrons'),
  PFTauTag = cms.InputTag('hpsPFTauProducer'),
  MuonTag = cms.InputTag('MyMuons'),
  PVTag = cms.InputTag('offlinePrimaryVertices'),
  mightGet = cms.optional.untracked.vstring
)
