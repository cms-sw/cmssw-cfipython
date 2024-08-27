import FWCore.ParameterSet.Config as cms

def TtSemiLepSignalSelMVAComputer(**kwargs):
  mod = cms.EDProducer('TtSemiLepSignalSelMVAComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
