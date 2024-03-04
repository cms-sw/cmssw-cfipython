import FWCore.ParameterSet.Config as cms

def DQMHcalPhiSymAlCaReco(**kwargs):
  mod = cms.EDProducer('DQMHcalPhiSymAlCaReco',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
