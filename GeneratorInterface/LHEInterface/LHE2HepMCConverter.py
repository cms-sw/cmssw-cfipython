import FWCore.ParameterSet.Config as cms

def LHE2HepMCConverter(*args, **kwargs):
  mod = cms.EDProducer('LHE2HepMCConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
