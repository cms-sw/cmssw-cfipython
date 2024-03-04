import FWCore.ParameterSet.Config as cms

def L1TStage2GlobalAlgBlkComparison(**kwargs):
  mod = cms.EDProducer('L1TStage2GlobalAlgBlkComparison',
    collection1 = cms.InputTag('collection1'),
    collection2 = cms.InputTag('collection2'),
    checkBxRange = cms.bool(True),
    checkCollSizePerBx = cms.bool(True),
    checkObject = cms.bool(True),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
