import FWCore.ParameterSet.Config as cms

def SchemaEvolutionSoAProducer(*args, **kwargs):
  mod = cms.EDProducer('SchemaEvolutionSoAProducer',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
