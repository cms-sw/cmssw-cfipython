import FWCore.ParameterSet.Config as cms

def LwtnnESProducer(**kwargs):
  mod = cms.ESProducer('LwtnnESProducer',
    ComponentName = cms.string('lwtnnESProducer'),
    fileName = cms.FileInPath(),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
