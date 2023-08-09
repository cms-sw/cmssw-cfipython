import FWCore.ParameterSet.Config as cms

tfGraphDefProducer = cms.ESProducer('TfGraphDefProducer',
  ComponentName = cms.string('tfGraphDef'),
  FileName = cms.FileInPath(''),
  appendToDataLabel = cms.string('')
)
