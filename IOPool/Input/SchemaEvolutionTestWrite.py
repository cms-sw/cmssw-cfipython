import FWCore.ParameterSet.Config as cms

def SchemaEvolutionTestWrite(**kwargs):
  mod = cms.EDProducer('SchemaEvolutionTestWrite',
    testIntegralValues = cms.required.vint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
