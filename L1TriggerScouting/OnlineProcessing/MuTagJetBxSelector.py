import FWCore.ParameterSet.Config as cms

def MuTagJetBxSelector(*args, **kwargs):
  mod = cms.EDProducer('MuTagJetBxSelector',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
