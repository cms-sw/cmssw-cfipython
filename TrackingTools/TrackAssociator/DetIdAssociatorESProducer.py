import FWCore.ParameterSet.Config as cms

def DetIdAssociatorESProducer(**kwargs):
  mod = cms.ESProducer('DetIdAssociatorESProducer',
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
