import FWCore.ParameterSet.Config as cms

def sistrip_MeasureLA(*args, **kwargs):
  mod = cms.ESProducer('sistrip::MeasureLA',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
