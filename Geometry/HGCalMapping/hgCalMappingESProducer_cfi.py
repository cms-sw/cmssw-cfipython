import FWCore.ParameterSet.Config as cms

hgCalMappingESProducer = cms.ESSource('HGCalMappingESProducer',
  modules = cms.required.FileInPath,
  si = cms.required.FileInPath,
  sipm = cms.required.FileInPath,
  appendToDataLabel = cms.string('')
)
