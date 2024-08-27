import FWCore.ParameterSet.Config as cms

def BasicHepMCHeavyIonValidation(**kwargs):
  mod = cms.EDProducer('BasicHepMCHeavyIonValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
