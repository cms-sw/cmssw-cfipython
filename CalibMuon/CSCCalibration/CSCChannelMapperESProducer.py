import FWCore.ParameterSet.Config as cms

def CSCChannelMapperESProducer(*args, **kwargs):
  mod = cms.ESProducer('CSCChannelMapperESProducer',
    AlgoName = cms.string('CSCChannelMapperStartup'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
