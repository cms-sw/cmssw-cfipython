import FWCore.ParameterSet.Config as cms

def L1TStage2Layer1Producer(**kwargs):
  mod = cms.EDProducer('L1TStage2Layer1Producer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
