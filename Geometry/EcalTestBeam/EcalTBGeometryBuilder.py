import FWCore.ParameterSet.Config as cms

def EcalTBGeometryBuilder(*args, **kwargs):
  mod = cms.ESProducer('EcalTBGeometryBuilder',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
