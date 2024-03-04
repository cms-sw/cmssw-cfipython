import FWCore.ParameterSet.Config as cms

def DQMHcalDiJetsAlCaReco(**kwargs):
  mod = cms.EDProducer('DQMHcalDiJetsAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
