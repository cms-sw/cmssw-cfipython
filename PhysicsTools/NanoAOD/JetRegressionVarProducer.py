import FWCore.ParameterSet.Config as cms

def JetRegressionVarProducer(**kwargs):
  mod = cms.EDProducer('JetRegressionVarProducer',
    src = cms.required.InputTag,
    pvsrc = cms.required.InputTag,
    svsrc = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
