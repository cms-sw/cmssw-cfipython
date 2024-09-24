import FWCore.ParameterSet.Config as cms

def L1TCtL2EgProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TCtL2EgProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
