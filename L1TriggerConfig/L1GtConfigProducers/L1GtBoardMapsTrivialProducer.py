import FWCore.ParameterSet.Config as cms

def L1GtBoardMapsTrivialProducer(**kwargs):
  mod = cms.ESProducer('L1GtBoardMapsTrivialProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
