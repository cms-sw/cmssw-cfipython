import FWCore.ParameterSet.Config as cms

def CSCObjectMapESProducer(*args, **kwargs):
  mod = cms.ESProducer('CSCObjectMapESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
