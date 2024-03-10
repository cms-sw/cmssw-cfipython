import FWCore.ParameterSet.Config as cms

def TfGraphDefProducer(**kwargs):
  mod = cms.ESProducer('TfGraphDefProducer',
    ComponentName = cms.string('tfGraphDef'),
    FileName = cms.FileInPath(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
