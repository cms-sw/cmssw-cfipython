import FWCore.ParameterSet.Config as cms

def TSGFromL1Muon(**kwargs):
  mod = cms.EDProducer('TSGFromL1Muon',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
