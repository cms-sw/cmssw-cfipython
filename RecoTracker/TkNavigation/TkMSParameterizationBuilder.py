import FWCore.ParameterSet.Config as cms

def TkMSParameterizationBuilder(**kwargs):
  mod = cms.ESProducer('TkMSParameterizationBuilder',
    navigationSchool = cms.string('SimpleNavigationSchool'),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
