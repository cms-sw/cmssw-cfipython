import FWCore.ParameterSet.Config as cms

def L1EmulatorErrorFlagClient(**kwargs):
  mod = cms.EDProducer('L1EmulatorErrorFlagClient',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
