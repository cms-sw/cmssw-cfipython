import FWCore.ParameterSet.Config as cms

def CSCChannelMapperESProducer(**kwargs):
  mod = cms.ESProducer('CSCChannelMapperESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
