import FWCore.ParameterSet.Config as cms

def XMLIdealGeometryESProducer(**kwargs):
  mod = cms.ESProducer('XMLIdealGeometryESProducer',
    rootDDName = cms.required.string,
    label = cms.required.string,
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
