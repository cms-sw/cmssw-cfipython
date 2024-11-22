import FWCore.ParameterSet.Config as cms

def SchemaEvolutionTestWrite(*args, **kwargs):
  mod = cms.EDProducer('SchemaEvolutionTestWrite',
    testIntegralValues = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
