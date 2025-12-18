import FWCore.ParameterSet.Config as cms

def PatElectronDRNCorrectionProducer(*args, **kwargs):
  mod = cms.EDProducer('PatElectronDRNCorrectionProducer',
    Client = cms.PSet(
      mode = cms.string('PseudoAsync'),
      allowedTries = cms.untracked.uint32(0),
      verbose = cms.untracked.bool(False),
      modelName = cms.required.string,
      modelVersion = cms.string(''),
      modelConfigPath = cms.required.FileInPath,
      preferredServer = cms.untracked.string(''),
      timeout = cms.required.untracked.uint32,
      timeoutUnit = cms.untracked.string('seconds'),
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
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
