import FWCore.ParameterSet.Config as cms

def L1TStage2uGTTiming(**kwargs):
  mod = cms.EDProducer('L1TStage2uGTTiming',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
