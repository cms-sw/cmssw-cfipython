import FWCore.ParameterSet.Config as cms

def CSCIndexerESProducer(*args, **kwargs):
  mod = cms.ESProducer('CSCIndexerESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
