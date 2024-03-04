import FWCore.ParameterSet.Config as cms

def LHE2HepMCConverter(**kwargs):
  mod = cms.EDProducer('LHE2HepMCConverter',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
