import FWCore.ParameterSet.Config as cms

def PFTauPrimaryVertexProducer(**kwargs):
  mod = cms.EDProducer('PFTauPrimaryVertexProducer',
    discriminators = cms.required.VPSet,
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
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
