import FWCore.ParameterSet.Config as cms

def HGCalTopologyBuilder(*args, **kwargs):
  mod = cms.ESProducer('HGCalTopologyBuilder',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
