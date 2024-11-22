import FWCore.ParameterSet.Config as cms

def NavigationSchoolESProducer(*args, **kwargs):
  mod = cms.ESProducer('NavigationSchoolESProducer',
    ComponentName = cms.required.string,
    PluginName = cms.string(''),
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
