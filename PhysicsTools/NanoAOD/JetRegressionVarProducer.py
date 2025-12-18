import FWCore.ParameterSet.Config as cms

def JetRegressionVarProducer(*args, **kwargs):
  mod = cms.EDProducer('JetRegressionVarProducer',
    src = cms.required.InputTag,
    pvsrc = cms.required.InputTag,
    svsrc = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
