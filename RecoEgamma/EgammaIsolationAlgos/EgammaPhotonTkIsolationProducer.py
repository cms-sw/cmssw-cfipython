import FWCore.ParameterSet.Config as cms

def EgammaPhotonTkIsolationProducer(**kwargs):
  mod = cms.EDProducer('EgammaPhotonTkIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
