import FWCore.ParameterSet.Config as cms

def CSCTFConfigProducer(*args, **kwargs):
  mod = cms.ESProducer('CSCTFConfigProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
