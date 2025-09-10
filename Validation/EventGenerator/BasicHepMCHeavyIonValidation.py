import FWCore.ParameterSet.Config as cms

def BasicHepMCHeavyIonValidation(*args, **kwargs):
  mod = cms.EDProducer('BasicHepMCHeavyIonValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
