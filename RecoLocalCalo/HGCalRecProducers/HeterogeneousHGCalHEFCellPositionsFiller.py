import FWCore.ParameterSet.Config as cms

def HeterogeneousHGCalHEFCellPositionsFiller(*args, **kwargs):
  mod = cms.ESProducer('HeterogeneousHGCalHEFCellPositionsFiller',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
