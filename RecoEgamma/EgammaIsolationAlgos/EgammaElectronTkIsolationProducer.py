import FWCore.ParameterSet.Config as cms

def EgammaElectronTkIsolationProducer(**kwargs):
  mod = cms.EDProducer('EgammaElectronTkIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
