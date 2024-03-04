import FWCore.ParameterSet.Config as cms

def PhotonAnalyzer(**kwargs):
  mod = cms.EDProducer('PhotonAnalyzer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
