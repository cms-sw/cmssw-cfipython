import FWCore.ParameterSet.Config as cms

alpaka_cuda_asyncEcalElectronicsMappingHostESProducer = cms.ESProducer('alpaka_cuda_async::EcalElectronicsMappingHostESProducer',
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
