import FWCore.ParameterSet.Config as cms

def sistrip_MeasureLA(**kwargs):
  mod = cms.ESProducer('sistrip::MeasureLA',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
