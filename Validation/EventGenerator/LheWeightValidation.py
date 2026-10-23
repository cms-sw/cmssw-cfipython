import FWCore.ParameterSet.Config as cms

def LheWeightValidation(*args, **kwargs):
  mod = cms.EDProducer('LheWeightValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
