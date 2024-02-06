import FWCore.ParameterSet.Config as cms

ecalMultifitConditionsHostESProducer = cms.ESProducer('EcalMultifitConditionsHostESProducer@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
