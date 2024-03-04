import FWCore.ParameterSet.Config as cms

def L1TStage2CPPF(**kwargs):
  mod = cms.EDProducer('L1TStage2CPPF',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
