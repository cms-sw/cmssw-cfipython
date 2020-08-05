import FWCore.ParameterSet.Config as cms

PATElectronProducer = cms.EDProducer('PATElectronProducer',
  pfCandidateMap = cms.InputTag('no default'),
  electronSource = cms.InputTag('no default'),
  addPFClusterIso = cms.bool(False),
  ecalPFClusterIsoMap = cms.InputTag(''),
  hcalPFClusterIsoMap = cms.InputTag(''),
  addPuppiIsolation = cms.bool(False),
  embedGsfElectronCore = cms.bool(True),
  embedGsfTrack = cms.bool(True),
  embedSuperCluster = cms.bool(True),
  embedPflowSuperCluster = cms.bool(True),
  embedSeedCluster = cms.bool(True),
  embedBasicClusters = cms.bool(True),
  embedPreshowerClusters = cms.bool(True),
  embedPflowBasicClusters = cms.bool(True),
  embedPflowPreshowerClusters = cms.bool(True),
  embedTrack = cms.bool(False),
  embedRecHits = cms.bool(True),
  pfElectronSource = cms.InputTag('pfElectrons'),
  usePfCandidateMultiMap = cms.bool(False),
  useParticleFlow = cms.bool(False),
  embedPFCandidate = cms.bool(False),
  addGenMatch = cms.bool(True),
  embedGenMatch = cms.bool(False),
  genParticleMatch = cms.InputTag(''),
  addElectronID = cms.bool(True),
  electronIDSource = cms.InputTag(''),
  computeMiniIso = cms.bool(False),
  pfCandsForMiniIso = cms.InputTag('packedPFCandidates'),
  miniIsoParamsE = cms.vdouble(),
  miniIsoParamsB = cms.vdouble(),
  isoDeposits = cms.PSet(),
  isolationValues = cms.PSet(),
  isolationValuesNoPFId = cms.PSet(),
  efficiencies = cms.PSet(),
  addEfficiencies = cms.bool(False),
  userData = cms.PSet(
    userClasses = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userFloats = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userInts = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userCands = cms.PSet(
      labelPostfixesToStrip = cms.vstring()
    ),
    userFunctions = cms.vstring(),
    userFunctionLabels = cms.vstring()
  ),
  addMVAVariables = cms.bool(True),
  reducedBarrelRecHitCollection = cms.InputTag('reducedEcalRecHitsEB'),
  reducedEndcapRecHitCollection = cms.InputTag('reducedEcalRecHitsEE'),
  userIsolation = cms.PSet(),
  addResolutions = cms.bool(False),
  resolutions = cms.PSet(),
  embedHighLevelSelection = cms.bool(True),
  beamLineSrc = cms.InputTag(''),
  pvSrc = cms.InputTag(''),
  getdBFromTrack = cms.bool(False)
)
