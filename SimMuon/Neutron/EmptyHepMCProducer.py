import FWCore.ParameterSet.Config as cms

def EmptyHepMCProducer(*args, **kwargs):
  mod = cms.EDProducer('EmptyHepMCProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
