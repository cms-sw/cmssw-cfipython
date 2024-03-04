import FWCore.ParameterSet.Config as cms

def BTagSFProducer(**kwargs):
  mod = cms.EDProducer('BTagSFProducer',
    src = cms.required.InputTag,
    cut = cms.required.string,
    discNames = cms.required.vstring,
    discShortNames = cms.required.vstring,
    weightFiles = cms.required.vstring,
    operatingPoints = cms.required.vstring,
    measurementTypesB = cms.required.vstring,
    measurementTypesC = cms.required.vstring,
    measurementTypesUDSG = cms.required.vstring,
    sysTypes = cms.required.vstring,
    validate = cms.untracked.bool(False),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
