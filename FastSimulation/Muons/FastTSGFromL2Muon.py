import FWCore.ParameterSet.Config as cms

def FastTSGFromL2Muon(**kwargs):
  mod = cms.EDProducer('FastTSGFromL2Muon',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
