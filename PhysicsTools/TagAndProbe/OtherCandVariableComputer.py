import FWCore.ParameterSet.Config as cms

def OtherCandVariableComputer(*args, **kwargs):
  mod = cms.EDProducer('OtherCandVariableComputer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
