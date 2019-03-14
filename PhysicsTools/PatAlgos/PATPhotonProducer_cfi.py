import FWCore.ParameterSet.Config as cms

PATPhotonProducer = cms.EDProducer('PATPhotonProducer',
  photonSource = cms.InputTag('no default'),
  electronSource = cms.InputTag('no default'),
  conversionSource = cms.InputTag('allConversions'),
  reducedBarrelRecHitCollection = cms.InputTag('reducedEcalRecHitsEB'),
  reducedEndcapRecHitCollection = cms.InputTag('reducedEcalRecHitsEE'),
  addPFClusterIso = cms.bool(False),
  ecalPFClusterIsoMap = cms.InputTag(''),
  hcalPFClusterIsoMap = cms.InputTag(''),
  addPuppiIsolation = cms.bool(False),
  embedSuperCluster = cms.bool(True),
  embedSeedCluster = cms.bool(True),
  embedBasicClusters = cms.bool(True),
  embedPreshowerClusters = cms.bool(True),
  embedRecHits = cms.bool(True),
  addGenMatch = cms.bool(True),
  embedGenMatch = cms.bool(False),
  genParticleMatch = cms.InputTag(''),
  addResolutions = cms.bool(False),
  resolutions = cms.PSet(),
  addPhotonID = cms.bool(True),
  photonIDSource = cms.InputTag(''),
  isoDeposits = cms.PSet(),
  isolationValues = cms.PSet(),
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
  userIsolation = cms.PSet(),
  beamLineSrc = cms.InputTag(''),
  saveRegressionData = cms.bool(True)
)
