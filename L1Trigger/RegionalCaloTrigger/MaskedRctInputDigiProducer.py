import FWCore.ParameterSet.Config as cms

def MaskedRctInputDigiProducer(*args, **kwargs):
  mod = cms.EDProducer('MaskedRctInputDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
