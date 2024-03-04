import FWCore.ParameterSet.Config as cms

def HGCalTBTopologyBuilder(**kwargs):
  mod = cms.ESProducer('HGCalTBTopologyBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
