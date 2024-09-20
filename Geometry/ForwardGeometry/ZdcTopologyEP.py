import FWCore.ParameterSet.Config as cms

def ZdcTopologyEP(**kwargs):
  mod = cms.ESProducer('ZdcTopologyEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
