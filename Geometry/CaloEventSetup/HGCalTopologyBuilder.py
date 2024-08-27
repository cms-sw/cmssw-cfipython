import FWCore.ParameterSet.Config as cms

def HGCalTopologyBuilder(**kwargs):
  mod = cms.ESProducer('HGCalTopologyBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
