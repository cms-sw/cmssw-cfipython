import FWCore.ParameterSet.Config as cms

def GenericMVAJetTagESProducer(*args, **kwargs):
  mod = cms.ESProducer('GenericMVAJetTagESProducer',
    useCategories = cms.bool(False),
    categoryVariableName = cms.string(''),
    calibrationRecords = cms.vstring(),
    calibrationRecord = cms.string(''),
    recordLabel = cms.string(''),
    appendToDataLabel = cms.string('')
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
