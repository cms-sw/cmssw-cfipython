import FWCore.ParameterSet.Config as cms

def testMaterialEffects(*args, **kwargs):
  mod = cms.EDProducer('testMaterialEffects',
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
