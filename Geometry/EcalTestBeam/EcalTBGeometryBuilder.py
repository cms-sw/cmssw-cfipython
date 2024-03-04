import FWCore.ParameterSet.Config as cms

def EcalTBGeometryBuilder(**kwargs):
  mod = cms.ESProducer('EcalTBGeometryBuilder',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
