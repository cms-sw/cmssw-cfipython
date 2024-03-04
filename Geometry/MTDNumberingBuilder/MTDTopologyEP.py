import FWCore.ParameterSet.Config as cms

def MTDTopologyEP(**kwargs):
  mod = cms.ESProducer('MTDTopologyEP',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
