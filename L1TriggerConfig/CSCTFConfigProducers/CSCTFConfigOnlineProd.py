import FWCore.ParameterSet.Config as cms

def CSCTFConfigOnlineProd(*args, **kwargs):
  mod = cms.ESProducer('CSCTFConfigOnlineProd',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
