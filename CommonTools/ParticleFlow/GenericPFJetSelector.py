import FWCore.ParameterSet.Config as cms

def GenericPFJetSelector(*args, **kwargs):
  mod = cms.EDFilter('GenericPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
