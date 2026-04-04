import FWCore.ParameterSet.Config as cms

def WhatsItESProducer(*args, **kwargs):
  mod = cms.ESProducer('WhatsItESProducer',
    doodadLabel = cms.optional.string,
    test = cms.untracked.bool(False),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
