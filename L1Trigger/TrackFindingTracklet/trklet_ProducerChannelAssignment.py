import FWCore.ParameterSet.Config as cms

def trklet_ProducerChannelAssignment(**kwargs):
  mod = cms.ESProducer('trklet::ProducerChannelAssignment',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
