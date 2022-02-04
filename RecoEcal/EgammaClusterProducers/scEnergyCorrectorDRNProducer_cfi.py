import FWCore.ParameterSet.Config as cms

scEnergyCorrectorDRNProducer = cms.EDProducer('SCEnergyCorrectorDRNProducer',
  correctorCfg = cms.PSet(
    ecalRecHitsEE = cms.InputTag('ecalRecHit', 'reducedEcalRecHitsEE'),
    ecalRecHitsEB = cms.InputTag('ecalRecHit', 'reducedEcalRecHitsEB'),
    rhoFastJet = cms.InputTag('fixedGridRhoAll')
  ),
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    modelName = cms.required.string,
    modelVersion = cms.string(''),
    modelConfigPath = cms.required.FileInPath,
    preferredServer = cms.untracked.string(''),
    timeout = cms.required.untracked.uint32,
    verbose = cms.untracked.bool(False),
    useSharedMemory = cms.untracked.bool(True),
    compression = cms.untracked.string(''),
    outputs = cms.untracked.vstring()
  ),
  inputSCs = cms.InputTag('particleFlowSuperClusterECAL'),
  mightGet = cms.optional.untracked.vstring
)