import FWCore.ParameterSet.Config as cms

alpaka_rocm_asyncEcalElectronicsMappingHostESProducer = cms.ESProducer('alpaka_rocm_async::EcalElectronicsMappingHostESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
