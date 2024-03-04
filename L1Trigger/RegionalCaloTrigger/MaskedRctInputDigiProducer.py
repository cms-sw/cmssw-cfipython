import FWCore.ParameterSet.Config as cms

def MaskedRctInputDigiProducer(**kwargs):
  mod = cms.EDProducer('MaskedRctInputDigiProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
