import FWCore.ParameterSet.Config as cms

def EtMinPFJetSelector(*args, **kwargs):
  mod = cms.EDFilter('EtMinPFJetSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
