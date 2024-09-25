import FWCore.ParameterSet.Config as cms

def HGCalNumberingInitialization(*args, **kwargs):
  mod = cms.ESProducer('HGCalNumberingInitialization',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
