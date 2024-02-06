import FWCore.ParameterSet.Config as cms

patElectronDRNCorrectionProducer = cms.EDProducer('PatElectronDRNCorrectionProducer',
  Client = cms.PSet(
    mode = cms.string('PseudoAsync'),
    allowedTries = cms.untracked.uint32(0),
    verbose = cms.untracked.bool(False),
    modelName = cms.required.string,
    modelVersion = cms.string(''),
    modelConfigPath = cms.required.FileInPath,
    preferredServer = cms.untracked.string(''),
    timeout = cms.required.untracked.uint32,
    useSharedMemory = cms.untracked.bool(True),
    compression = cms.untracked.string(''),
    outputs = cms.untracked.vstring()
  ),
  particleSource = cms.required.InputTag,
  rhoName = cms.required.InputTag,
  reducedEcalRecHitsEB = cms.InputTag('reducedEcalRecHitsEB'),
  reducedEcalRecHitsEE = cms.InputTag('reducedEcalRecHitsEE'),
  reducedEcalRecHitsES = cms.InputTag('reducedEcalRecHitsES'),
  mightGet = cms.optional.untracked.vstring
)
