import FWCore.ParameterSet.Config as cms

def SUSY_HLT_Muon_Hadronic(*args, **kwargs):
  mod = cms.EDProducer('SUSY_HLT_Muon_Hadronic',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
