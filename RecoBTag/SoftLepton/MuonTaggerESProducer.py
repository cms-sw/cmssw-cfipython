import FWCore.ParameterSet.Config as cms

def MuonTaggerESProducer(**kwargs):
  mod = cms.ESProducer('MuonTaggerESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
