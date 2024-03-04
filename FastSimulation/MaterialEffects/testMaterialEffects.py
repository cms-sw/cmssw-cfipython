import FWCore.ParameterSet.Config as cms

def testMaterialEffects(**kwargs):
  mod = cms.EDProducer('testMaterialEffects',
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
