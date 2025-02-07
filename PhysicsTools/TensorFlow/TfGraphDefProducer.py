import FWCore.ParameterSet.Config as cms

def TfGraphDefProducer(*args, **kwargs):
  mod = cms.ESProducer('TfGraphDefProducer',
    ComponentName = cms.string('tfGraphDef'),
    FileName = cms.FileInPath(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
