import FWCore.ParameterSet.Config as cms

def EgammaPhotonTkNumIsolationProducer(**kwargs):
  mod = cms.EDProducer('EgammaPhotonTkNumIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
