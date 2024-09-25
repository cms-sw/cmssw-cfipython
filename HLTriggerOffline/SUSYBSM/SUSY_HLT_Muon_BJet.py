import FWCore.ParameterSet.Config as cms

def SUSY_HLT_Muon_BJet(*args, **kwargs):
  mod = cms.EDProducer('SUSY_HLT_Muon_BJet',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
