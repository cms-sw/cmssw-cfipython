import FWCore.ParameterSet.Config as cms

hgcalHGCalMappingModuleESProducer = cms.ESProducer('hgcal::HGCalMappingModuleESProducer@alpaka',
  filename = cms.required.FileInPath,
  moduleindexer = cms.ESInputTag('', ''),
  appendToDataLabel = cms.string(''),
  alpaka = cms.untracked.PSet(
    backend = cms.untracked.string('')
  )
)
