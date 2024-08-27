import FWCore.ParameterSet.Config as cms

def PatElectronEAIsoCorrectionProducer(**kwargs):
  mod = cms.EDProducer('PatElectronEAIsoCorrectionProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
