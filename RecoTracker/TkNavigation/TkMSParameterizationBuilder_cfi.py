import FWCore.ParameterSet.Config as cms

TkMSParameterizationBuilder = cms.ESProducer('TkMSParameterizationBuilder',
  navigationSchool = cms.string('SimpleNavigationSchool'),
  appendToDataLabel = cms.string('')
)
