import FWCore.ParameterSet.Config as cms

def SUSY_HLT_Electron_BJet(*args, **kwargs):
  mod = cms.EDProducer('SUSY_HLT_Electron_BJet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
