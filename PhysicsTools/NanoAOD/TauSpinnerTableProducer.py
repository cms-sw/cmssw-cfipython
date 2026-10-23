import FWCore.ParameterSet.Config as cms

def TauSpinnerTableProducer(*args, **kwargs):
  mod = cms.EDProducer('TauSpinnerTableProducer',
    src = cms.required.InputTag,
    name = cms.required.string,
    theta = cms.required.vdouble,
    bosonPdgId = cms.int32(25),
    defaultWeight = cms.double(1),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
