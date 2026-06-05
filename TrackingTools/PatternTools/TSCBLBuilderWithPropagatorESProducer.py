import FWCore.ParameterSet.Config as cms

def TSCBLBuilderWithPropagatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('TSCBLBuilderWithPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
