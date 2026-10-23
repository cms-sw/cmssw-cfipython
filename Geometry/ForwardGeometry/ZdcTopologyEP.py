import FWCore.ParameterSet.Config as cms

def ZdcTopologyEP(*args, **kwargs):
  mod = cms.ESProducer('ZdcTopologyEP',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
