import FWCore.ParameterSet.Config as cms

def HGCalTBTopologyBuilder(*args, **kwargs):
  mod = cms.ESProducer('HGCalTBTopologyBuilder',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
