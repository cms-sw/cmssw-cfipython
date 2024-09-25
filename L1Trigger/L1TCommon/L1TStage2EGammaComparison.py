import FWCore.ParameterSet.Config as cms

def L1TStage2EGammaComparison(*args, **kwargs):
  mod = cms.EDProducer('L1TStage2EGammaComparison',
    collection1 = cms.InputTag('collection1'),
    collection2 = cms.InputTag('collection2'),
    checkBxRange = cms.bool(True),
    checkCollSizePerBx = cms.bool(True),
    checkObject = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
