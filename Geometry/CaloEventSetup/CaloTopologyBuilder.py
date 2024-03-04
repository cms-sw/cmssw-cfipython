import FWCore.ParameterSet.Config as cms

def CaloTopologyBuilder(**kwargs):
  mod = cms.ESProducer('CaloTopologyBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
