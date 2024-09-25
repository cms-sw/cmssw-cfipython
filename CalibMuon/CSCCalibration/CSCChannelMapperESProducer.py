import FWCore.ParameterSet.Config as cms

def CSCChannelMapperESProducer(*args, **kwargs):
  mod = cms.ESProducer('CSCChannelMapperESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
