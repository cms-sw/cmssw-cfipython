import FWCore.ParameterSet.Config as cms

def trklet_ProducerChannelAssignment(*args, **kwargs):
  mod = cms.ESProducer('trklet::ProducerChannelAssignment',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
