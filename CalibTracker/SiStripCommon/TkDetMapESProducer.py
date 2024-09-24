import FWCore.ParameterSet.Config as cms

def TkDetMapESProducer(**kwargs):
  mod = cms.ESProducer('TkDetMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod