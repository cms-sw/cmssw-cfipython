import FWCore.ParameterSet.Config as cms

def CandSecondaryVertexProducer(**kwargs):
  mod = cms.EDProducer('CandSecondaryVertexProducer',
    extSVDeltaRToJet = cms.double(0.3),
    beamSpotTag = cms.InputTag('offlineBeamSpot'),
    vertexReco = cms.PSet(
      primcut = cms.double(1.8),
      seccut = cms.double(6),
      finder = cms.string('avr'),
      minweight = cms.double(0.5),
      weightthreshold = cms.double(0.001),
      smoothing = cms.bool(False),
      maxFitChi2 = cms.double(10),
      mergeThreshold = cms.double(3),
      fitType = cms.string('RefitGhostTrackWithVertices')
    ),
    vertexSelection = cms.PSet(
      sortCriterium = cms.string('dist3dError')
    ),
    constraint = cms.string('BeamSpot'),
    trackIPTagInfos = cms.InputTag('impactParameterTagInfos'),
    vertexCuts = cms.PSet(
      distSig3dMax = cms.double(99999.9),
      fracPV = cms.double(0.65),
      distVal2dMax = cms.double(2.5),
      useTrackWeights = cms.bool(True),
      maxDeltaRToJetAxis = cms.double(0.4),
      v0Filter = cms.PSet(
        k0sMassWindow = cms.double(0.05)
      ),
      distSig2dMin = cms.double(3),
      multiplicityMin = cms.uint32(2),
      distVal2dMin = cms.double(0.01),
      distSig2dMax = cms.double(99999.9),
      distVal3dMax = cms.double(99999.9),
      minimumTrackWeight = cms.double(0.5),
      distVal3dMin = cms.double(-99999.9),
      massMax = cms.double(6.5),
      distSig3dMin = cms.double(-99999.9)
    ),
    useExternalSV = cms.bool(False),
    minimumTrackWeight = cms.double(0.5),
    usePVError = cms.bool(True),
    trackSelection = cms.PSet(
      b_pT = cms.double(0.3684),
      max_pT = cms.double(500),
      useVariableJTA = cms.bool(False),
      maxDecayLen = cms.double(99999.9),
      sip3dValMin = cms.double(-99999.9),
      max_pT_dRcut = cms.double(0.1),
      a_pT = cms.double(0.005263),
      totalHitsMin = cms.uint32(8),
      jetDeltaRMax = cms.double(0.3),
      a_dR = cms.double(-0.001053),
      maxDistToAxis = cms.double(0.2),
      ptMin = cms.double(1),
      qualityClass = cms.string('any'),
      pixelHitsMin = cms.uint32(2),
      sip2dValMax = cms.double(99999.9),
      max_pT_trackPTcut = cms.double(3),
      sip2dValMin = cms.double(-99999.9),
      normChi2Max = cms.double(99999.9),
      sip3dValMax = cms.double(99999.9),
      sip3dSigMin = cms.double(-99999.9),
      min_pT = cms.double(120),
      min_pT_dRcut = cms.double(0.5),
      sip2dSigMax = cms.double(99999.9),
      sip3dSigMax = cms.double(99999.9),
      sip2dSigMin = cms.double(-99999.9),
      b_dR = cms.double(0.6263)
    ),
    trackSort = cms.string('sip3dSig'),
    extSVCollection = cms.InputTag('secondaryVertices'),
    useSVClustering = cms.bool(False),
    jetAlgorithm = cms.optional.string,
    rParam = cms.optional.double,
    useSVMomentum = cms.bool(False),
    ghostRescaling = cms.double(1e-18),
    relPtTolerance = cms.double(0.001),
    fatJets = cms.optional.InputTag,
    groomedFatJets = cms.optional.InputTag,
    weights = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
