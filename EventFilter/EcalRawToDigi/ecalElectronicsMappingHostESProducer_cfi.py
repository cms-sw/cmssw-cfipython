import FWCore.ParameterSet.Config as cms

ecalElectronicsMappingHostESProducer = cms.ESProducer('EcalElectronicsMappingHostESProducer@alpaka',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
