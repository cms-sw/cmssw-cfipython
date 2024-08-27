import FWCore.ParameterSet.Config as cms

def HeterogeneousHGCalHEFCellPositionsFiller(**kwargs):
  mod = cms.ESProducer('HeterogeneousHGCalHEFCellPositionsFiller',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
