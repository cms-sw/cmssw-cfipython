import FWCore.ParameterSet.Config as cms

def TSCBLBuilderWithPropagatorESProducer(**kwargs):
  mod = cms.ESProducer('TSCBLBuilderWithPropagatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
