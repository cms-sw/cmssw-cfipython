import FWCore.ParameterSet.Config as cms

def RecoTauPiZeroProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoTauPiZeroProducer',
    massHypothesis = cms.double(0.136),
    ranking = cms.VPSet(
      cms.PSet(
        name = cms.string(''),
        plugin = cms.string(''),
        selection = cms.string(''),
        selectionFailValue = cms.double(1000),
        selectionPassFunction = cms.string('')
      ),
      template = cms.PSetTemplate(
        selectionPassFunction = cms.string('Func'),
        selectionFailValue = cms.double(1000),
        selection = cms.string('Sel'),
        name = cms.string('name'),
        plugin = cms.string('plugin')
      )
    ),
    verbosity = cms.int32(0),
    maxJetAbsEta = cms.double(2.5),
    outputSelection = cms.string('pt > 0'),
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
        stripPhiAssociationDistanceFunc = cms.PSet(
          function = cms.string('TMath::Min(0.3, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
          par1 = cms.double(0.707716),
          par0 = cms.double(0.352476)
        ),
        stripEtaAssociationDistanceFunc = cms.PSet(
          function = cms.string('TMath::Min(0.15, TMath::Max(0.05, [0]*TMath::Power(pT, -[1])))'),
          par1 = cms.double(0.658701),
          par0 = cms.double(0.197077)
        ),
        stripEtaAssociationDistance = cms.double(0.05),
        stripPhiAssociationDistance = cms.double(0.2),
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
        name = cms.required.string,
        plugin = cms.required.string,
        verbosity = cms.int32(0),
        makeCombinatoricStrips = cms.optional.bool,
        maxStripBuildIterations = cms.optional.int32,
        minGammaEtStripAdd = cms.optional.double,
        minGammaEtStripSeed = cms.optional.double,
        minStripEt = cms.optional.double,
        stripCandidatesParticleIds = cms.optional.vint32,
        updateStripAfterEachDaughter = cms.optional.bool,
        applyElecTrackQcuts = cms.optional.bool
      )
    ),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
