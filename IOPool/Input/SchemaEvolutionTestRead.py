import FWCore.ParameterSet.Config as cms

def SchemaEvolutionTestRead(**kwargs):
  mod = cms.EDAnalyzer('SchemaEvolutionTestRead',
    expectedVectorVectorIntegralValues = cms.required.vint32,
    vectorVectorTag = cms.required.InputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
