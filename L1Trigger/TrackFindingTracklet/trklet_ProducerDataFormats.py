import FWCore.ParameterSet.Config as cms

def trklet_ProducerDataFormats(*args, **kwargs):
  mod = cms.ESProducer('trklet::ProducerDataFormats',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
