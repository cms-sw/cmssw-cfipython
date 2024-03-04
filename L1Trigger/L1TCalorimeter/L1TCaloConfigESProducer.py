import FWCore.ParameterSet.Config as cms

def L1TCaloConfigESProducer(**kwargs):
  mod = cms.ESProducer('L1TCaloConfigESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
