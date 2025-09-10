import FWCore.ParameterSet.Config as cms

def LwtnnESProducer(*args, **kwargs):
  mod = cms.ESProducer('LwtnnESProducer',
    ComponentName = cms.string('lwtnnESProducer'),
    fileName = cms.FileInPath(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
