import FWCore.ParameterSet.Config as cms

def ElectronTaggerESProducer(**kwargs):
  mod = cms.ESProducer('ElectronTaggerESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
