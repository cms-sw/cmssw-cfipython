import FWCore.ParameterSet.Config as cms

def EgammaPhotonTkIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaPhotonTkIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
