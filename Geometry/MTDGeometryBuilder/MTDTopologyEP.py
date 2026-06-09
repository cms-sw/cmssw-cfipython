import FWCore.ParameterSet.Config as cms

def MTDTopologyEP(*args, **kwargs):
  mod = cms.ESProducer('MTDTopologyEP',
    isFull = cms.bool(True),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
