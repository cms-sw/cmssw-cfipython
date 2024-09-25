import FWCore.ParameterSet.Config as cms

def DetIdAssociatorESProducer(*args, **kwargs):
  mod = cms.ESProducer('DetIdAssociatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
