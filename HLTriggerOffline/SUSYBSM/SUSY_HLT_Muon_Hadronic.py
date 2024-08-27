import FWCore.ParameterSet.Config as cms

def SUSY_HLT_Muon_Hadronic(**kwargs):
  mod = cms.EDProducer('SUSY_HLT_Muon_Hadronic',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
