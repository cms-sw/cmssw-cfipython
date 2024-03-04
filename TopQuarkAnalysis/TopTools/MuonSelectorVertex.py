import FWCore.ParameterSet.Config as cms

def MuonSelectorVertex(**kwargs):
  mod = cms.EDProducer('MuonSelectorVertex',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
