import FWCore.ParameterSet.Config as cms

def PFRecoTauChargedHadronProducer(*args, **kwargs):
  mod = cms.EDProducer('PFRecoTauChargedHadronProducer',
    ranking = cms.VPSet(
      cms.PSet(
        name = cms.string('ChargedPFCandidate'),
        plugin = cms.string('PFRecoTauChargedHadronStringQuality'),
        selection = cms.string('algoIs("kChargedPFCandidate")'),
        selectionFailValue = cms.double(1000),
        selectionPassFunction = cms.string('-pt')
      ),
      template = cms.PSetTemplate(
        selectionPassFunction = cms.string('-pt'),
        selectionFailValue = cms.double(1000),
        selection = cms.string('algoIs("kChargedPFCandidate")'),
        name = cms.string('ChargedPFCandidate'),
        plugin = cms.string('PFRecoTauChargedHadronStringQuality')
      )
    ),
    verbosity = cms.int32(0),
    maxJetAbsEta = cms.double(2.5),
    outputSelection = cms.string('pt > 0.5'),
    minJetPt = cms.double(14),
    jetSrc = cms.InputTag('ak4PFJets'),
    builders = cms.VPSet(
      cms.PSet(
        name = cms.string(''),
        plugin = cms.string(''),
        verbosity = cms.int32(0),
        qualityCuts = cms.PSet()
      ),
      template = cms.PSetTemplate(
        minMergeChargedHadronPt = cms.required.double,
        name = cms.required.string,
        plugin = cms.required.string,
        dRcone = cms.optional.double,
        dRconeLimitedToJetArea = cms.optional.bool,
        dRmergeNeutralHadron = cms.optional.double,
        dRmergePhoton = cms.optional.double,
        srcTracks = cms.optional.InputTag,
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
        minMergeGammaEt = cms.required.double,
        verbosity = cms.int32(0),
        minMergeNeutralHadronEt = cms.required.double,
        dRmergePhotonWrtChargedHadron = cms.optional.double,
        dRmergePhotonWrtNeutralHadron = cms.optional.double,
        maxUnmatchedBlockElementsNeutralHadron = cms.optional.int32,
        dRmergePhotonWrtElectron = cms.optional.double,
        chargedHadronCandidatesParticleIds = cms.optional.vint32,
        minBlockElementMatchesPhoton = cms.optional.int32,
        dRmergeNeutralHadronWrtNeutralHadron = cms.optional.double,
        maxUnmatchedBlockElementsPhoton = cms.optional.int32,
        dRmergeNeutralHadronWrtOther = cms.optional.double,
        dRmergeNeutralHadronWrtElectron = cms.optional.double,
        minBlockElementMatchesNeutralHadron = cms.optional.int32,
        dRmergePhotonWrtOther = cms.optional.double,
        dRmergeNeutralHadronWrtChargedHadron = cms.optional.double
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
