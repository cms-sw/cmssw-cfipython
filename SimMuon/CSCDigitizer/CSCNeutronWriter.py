import FWCore.ParameterSet.Config as cms

def CSCNeutronWriter(*args, **kwargs):
  mod = cms.EDProducer('CSCNeutronWriter',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
