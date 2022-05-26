import FWCore.ParameterSet.Config as cms

tfGraphDefProducer = cms.ESProducer('TfGraphDefProducer',
  ComponentName = cms.string('tfGraphDef'),
  FileName = cms.required.FileInPath,
  appendToDataLabel = cms.string('')
)
