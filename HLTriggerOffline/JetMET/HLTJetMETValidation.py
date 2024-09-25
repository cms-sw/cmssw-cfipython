import FWCore.ParameterSet.Config as cms

def HLTJetMETValidation(*args, **kwargs):
  mod = cms.EDProducer('HLTJetMETValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
