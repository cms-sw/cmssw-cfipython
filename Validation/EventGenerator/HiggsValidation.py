import FWCore.ParameterSet.Config as cms

def HiggsValidation(*args, **kwargs):
  mod = cms.EDProducer('HiggsValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
