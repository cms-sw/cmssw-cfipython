import FWCore.ParameterSet.Config as cms

def ConfigurableAPVCyclePhaseProducer(*args, **kwargs):
  mod = cms.EDProducer('ConfigurableAPVCyclePhaseProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
