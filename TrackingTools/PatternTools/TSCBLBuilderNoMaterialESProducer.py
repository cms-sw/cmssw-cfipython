import FWCore.ParameterSet.Config as cms

def TSCBLBuilderNoMaterialESProducer(*args, **kwargs):
  mod = cms.ESProducer('TSCBLBuilderNoMaterialESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
