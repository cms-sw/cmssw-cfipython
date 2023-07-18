import FWCore.ParameterSet.Config as cms

ecalPhase2DigiToGPUProducer = cms.EDProducer('EcalPhase2DigiToGPUProducer',
  BarrelDigis = cms.InputTag('simEcalUnsuppressedDigis'),
  digisLabelEB = cms.string('ebDigis'),
  mightGet = cms.optional.untracked.vstring
)
