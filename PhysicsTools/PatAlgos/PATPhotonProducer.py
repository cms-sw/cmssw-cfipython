import FWCore.ParameterSet.Config as cms

def PATPhotonProducer(*args, **kwargs):
  mod = cms.EDProducer('PATPhotonProducer',
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
    isoDeposits = cms.PSet(
      tracker = cms.optional.InputTag,
      ecal = cms.optional.InputTag,
      hcal = cms.optional.InputTag,
      pfAllParticles = cms.optional.InputTag,
      pfChargedHadrons = cms.optional.InputTag,
      pfChargedAll = cms.optional.InputTag,
      pfPUChargedHadrons = cms.optional.InputTag,
      pfNeutralHadrons = cms.optional.InputTag,
      pfPhotons = cms.optional.InputTag,
      user = cms.optional.VInputTag
    ),
    isolationValues = cms.PSet(
      tracker = cms.optional.InputTag,
      ecal = cms.optional.InputTag,
      hcal = cms.optional.InputTag,
      pfAllParticles = cms.optional.InputTag,
      pfChargedHadrons = cms.optional.InputTag,
      pfChargedAll = cms.optional.InputTag,
      pfPUChargedHadrons = cms.optional.InputTag,
      pfNeutralHadrons = cms.optional.InputTag,
      pfPhotons = cms.optional.InputTag,
      user = cms.optional.VInputTag
    ),
    efficiencies = cms.PSet(),
    addEfficiencies = cms.bool(False),
    userData = cms.PSet(
      userClasses = cms.PSet(
        src = cms.required.VInputTag,
        labelPostfixesToStrip = cms.vstring()
      ),
      userFloats = cms.PSet(
        src = cms.required.VInputTag,
        labelPostfixesToStrip = cms.vstring()
      ),
      userInts = cms.PSet(
        src = cms.required.VInputTag,
        labelPostfixesToStrip = cms.vstring()
      ),
      userCands = cms.PSet(
        src = cms.required.VInputTag,
        labelPostfixesToStrip = cms.vstring()
      ),
      userFunctions = cms.vstring(),
      userFunctionLabels = cms.vstring()
    ),
    userIsolation = cms.PSet(),
    beamLineSrc = cms.InputTag(''),
    saveRegressionData = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
