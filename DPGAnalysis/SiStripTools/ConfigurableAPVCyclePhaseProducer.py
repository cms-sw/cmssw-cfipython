import FWCore.ParameterSet.Config as cms

def ConfigurableAPVCyclePhaseProducer(**kwargs):
  mod = cms.EDProducer('ConfigurableAPVCyclePhaseProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
