import FWCore.ParameterSet.Config as cms

def EgammaElectronTkIsolationProducer(*args, **kwargs):
  mod = cms.EDProducer('EgammaElectronTkIsolationProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
