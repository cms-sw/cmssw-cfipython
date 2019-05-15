import FWCore.ParameterSet.Config as cms

gemRecHitsDef = cms.EDProducer('GEMRecHitProducer',
  recAlgoConfig = cms.PSet(),
  recAlgo = cms.string('GEMRecHitStandardAlgo'),
  gemDigiLabel = cms.InputTag('muonGEMDigis'),
  applyMasking = cms.bool(False)
)
