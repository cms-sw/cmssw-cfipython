import FWCore.ParameterSet.Config as cms

def ElectronTaggerESProducer(*args, **kwargs):
  mod = cms.ESProducer('ElectronTaggerESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
