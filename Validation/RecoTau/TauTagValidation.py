import FWCore.ParameterSet.Config as cms

def TauTagValidation(**kwargs):
  mod = cms.EDProducer('TauTagValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
