import FWCore.ParameterSet.Config as cms

def OtherCandVariableComputer(**kwargs):
  mod = cms.EDProducer('OtherCandVariableComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
