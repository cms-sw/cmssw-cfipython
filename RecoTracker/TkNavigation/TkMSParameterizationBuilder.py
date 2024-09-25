import FWCore.ParameterSet.Config as cms

def TkMSParameterizationBuilder(*args, **kwargs):
  mod = cms.ESProducer('TkMSParameterizationBuilder',
    navigationSchool = cms.string('SimpleNavigationSchool'),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
