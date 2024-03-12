import FWCore.ParameterSet.Config as cms

lwtnnESProducer = cms.ESProducer('LwtnnESProducer',
  ComponentName = cms.string('lwtnnESProducer'),
  fileName = cms.FileInPath(''),
  appendToDataLabel = cms.string('')
)
