import FWCore.ParameterSet.Config as cms

def L1TdeStage2RegionalShower(*args, **kwargs):
  mod = cms.EDProducer('L1TdeStage2RegionalShower',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
