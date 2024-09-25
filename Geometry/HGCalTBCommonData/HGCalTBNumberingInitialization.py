import FWCore.ParameterSet.Config as cms

def HGCalTBNumberingInitialization(*args, **kwargs):
  mod = cms.ESProducer('HGCalTBNumberingInitialization',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
