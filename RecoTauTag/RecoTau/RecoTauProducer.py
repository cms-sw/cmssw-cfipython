import FWCore.ParameterSet.Config as cms

def RecoTauProducer(*args, **kwargs):
  mod = cms.EDProducer('RecoTauProducer',
    piZeroSrc = cms.InputTag('ak4PFJetsRecoTauPiZeros'),
    modifiers = cms.required.VPSet,
    jetRegionSrc = cms.InputTag('recoTauAK4PFJets08Region'),
    maxJetAbsEta = cms.double(2.5),
    outputSelection = cms.string('leadPFChargedHadrCand().isNonnull()'),
    chargedHadronSrc = cms.InputTag('ak4PFJetsRecoTauChargedHadrons'),
    minJetPt = cms.double(14),
    jetSrc = cms.InputTag('ak4PFJets'),
    builders = cms.VPSet(
      cms.PSet(
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        name = cms.string(''),
        pfCandSrc = cms.InputTag('particleFlow'),
        plugin = cms.string(''),
        verbosity = cms.int32(0)
      ),
      template = cms.PSetTemplate(
        name = cms.required.string,
        plugin = cms.required.string,
        verbosity = cms.int32(0),
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
        decayModes = cms.optional.VPSet,
        minAbsPhotonSumPt_insideSignalCone = cms.double(2.5),
        minRelPhotonSumPt_insideSignalCone = cms.double(0.1),
        pfCandSrc = cms.InputTag('particleFlow'),
        signalConeSize = cms.optional.string,
        isolationConeSize = cms.optional.double,
        minAbsPhotonSumPt_outsideSignalCone = cms.optional.double,
        minRelPhotonSumPt_outsideSignalCone = cms.optional.double,
        isoConeChargedHadrons = cms.optional.string,
        isoConeNeutralHadrons = cms.optional.string,
        isoConePiZeros = cms.optional.string,
        leadObjectPt = cms.optional.double,
        matchingCone = cms.optional.string,
        maxSignalConeChargedHadrons = cms.optional.int32,
        signalConeChargedHadrons = cms.optional.string,
        signalConeNeutralHadrons = cms.optional.string,
        signalConePiZeros = cms.optional.string,
        usePFLeptons = cms.optional.bool
      )
    ),
    buildNullTaus = cms.bool(False),
    verbosity = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
