import FWCore.ParameterSet.Config as cms

def L1TdeStage2RegionalShower(**kwargs):
  mod = cms.EDProducer('L1TdeStage2RegionalShower',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
