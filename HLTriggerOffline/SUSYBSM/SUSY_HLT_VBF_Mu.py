import FWCore.ParameterSet.Config as cms

def SUSY_HLT_VBF_Mu(*args, **kwargs):
  mod = cms.EDProducer('SUSY_HLT_VBF_Mu',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
