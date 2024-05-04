import FWCore.ParameterSet.Config as cms

alpaka_rocm_asynchgcalHGCalMappingModuleESProducer = cms.ESProducer('alpaka_rocm_async::hgcal::HGCalMappingModuleESProducer',
  filename = cms.required.FileInPath,
  moduleindexer = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
