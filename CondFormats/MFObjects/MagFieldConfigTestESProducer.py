import FWCore.ParameterSet.Config as cms

def MagFieldConfigTestESProducer(*args, **kwargs):
  mod = cms.ESProducer('MagFieldConfigTestESProducer',
    configs = cms.VPSet(
    ),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
