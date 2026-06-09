import FWCore.ParameterSet.Config as cms

def DDCompactViewMFESProducer(*args, **kwargs):
  mod = cms.ESProducer('DDCompactViewMFESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
