import FWCore.ParameterSet.Config as cms

gemRecHitsDef = cms.EDProducer('GEMRecHitProducer',
  recAlgoConfig = cms.PSet(),
  recAlgo = cms.string('GEMRecHitStandardAlgo'),
  gemDigiLabel = cms.InputTag('muonGEMDigis'),
  applyMasking = cms.bool(False),
  maskFile = cms.optional.FileInPath,
  deadFile = cms.optional.FileInPath,
  mightGet = cms.optional.untracked.vstring
)
