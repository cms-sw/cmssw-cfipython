import FWCore.ParameterSet.Config as cms

def TtSemiLepSignalSelMVAComputer(*args, **kwargs):
  mod = cms.EDProducer('TtSemiLepSignalSelMVAComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
