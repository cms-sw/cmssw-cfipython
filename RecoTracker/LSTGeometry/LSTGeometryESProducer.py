import FWCore.ParameterSet.Config as cms

def LSTGeometryESProducer(*args, **kwargs):
  mod = cms.ESProducer('LSTGeometryESProducer',
    ptCut = cms.double(0.8),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
