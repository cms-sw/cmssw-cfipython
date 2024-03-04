import FWCore.ParameterSet.Config as cms

def TtFullHadSignalSelMVAComputer(**kwargs):
  mod = cms.EDProducer('TtFullHadSignalSelMVAComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
