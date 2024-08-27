import FWCore.ParameterSet.Config as cms

def BasicHepMCValidation(**kwargs):
  mod = cms.EDProducer('BasicHepMCValidation',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
