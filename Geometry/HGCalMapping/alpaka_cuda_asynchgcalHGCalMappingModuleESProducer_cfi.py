import FWCore.ParameterSet.Config as cms

alpaka_cuda_asynchgcalHGCalMappingModuleESProducer = cms.ESProducer('alpaka_cuda_async::hgcal::HGCalMappingModuleESProducer',
  filename = cms.required.FileInPath,
  moduleindexer = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
