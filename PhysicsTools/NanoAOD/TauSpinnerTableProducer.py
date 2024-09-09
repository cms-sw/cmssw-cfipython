import FWCore.ParameterSet.Config as cms

def TauSpinnerTableProducer(**kwargs):
  mod = cms.EDProducer('TauSpinnerTableProducer',
    src = cms.required.InputTag,
    name = cms.required.string,
    theta = cms.required.vdouble,
    bosonPdgId = cms.int32(25),
    defaultWeight = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
