import FWCore.ParameterSet.Config as cms

def L1HLTJetsMatching(**kwargs):
  mod = cms.EDProducer('L1HLTJetsMatching',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
