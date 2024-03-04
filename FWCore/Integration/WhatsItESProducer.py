import FWCore.ParameterSet.Config as cms

def WhatsItESProducer(**kwargs):
  mod = cms.ESProducer('WhatsItESProducer',
    doodadLabel = cms.optional.string,
    test = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
