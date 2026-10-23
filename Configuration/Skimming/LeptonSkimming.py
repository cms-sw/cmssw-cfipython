import FWCore.ParameterSet.Config as cms

def LeptonSkimming(*args, **kwargs):
  mod = cms.EDFilter('LeptonSkimming',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
