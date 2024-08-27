import FWCore.ParameterSet.Config as cms

def SCEnergyCorrectorDRNProducer(**kwargs):
  mod = cms.EDProducer('SCEnergyCorrectorDRNProducer',
    correctorCfg = cms.PSet(
      ecalRecHitsEE = cms.InputTag('ecalRecHit', 'reducedEcalRecHitsEE'),
      ecalRecHitsEB = cms.InputTag('ecalRecHit', 'reducedEcalRecHitsEB'),
      rhoFastJet = cms.InputTag('fixedGridRhoAll')
    ),
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
    inputSCs = cms.InputTag('particleFlowSuperClusterECAL'),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
