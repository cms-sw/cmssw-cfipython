import FWCore.ParameterSet.Config as cms

def NavigationSchoolESProducer(**kwargs):
  mod = cms.ESProducer('NavigationSchoolESProducer',
    ComponentName = cms.required.string,
    PluginName = cms.string(''),
    SimpleMagneticField = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
