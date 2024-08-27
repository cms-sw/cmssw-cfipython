import FWCore.ParameterSet.Config as cms

def MagFieldConfigTestESProducer(**kwargs):
  mod = cms.ESProducer('MagFieldConfigTestESProducer',
    configs = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
