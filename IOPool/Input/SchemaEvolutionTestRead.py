import FWCore.ParameterSet.Config as cms

def SchemaEvolutionTestRead(*args, **kwargs):
  mod = cms.EDAnalyzer('SchemaEvolutionTestRead',
    expectedVectorVectorIntegralValues = cms.required.vint32,
    vectorVectorTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
