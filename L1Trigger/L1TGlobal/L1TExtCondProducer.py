import FWCore.ParameterSet.Config as cms

def L1TExtCondProducer(*args, **kwargs):
  mod = cms.EDProducer('L1TExtCondProducer',
    setBptxMinus = cms.bool(True),
    setBptxAND = cms.bool(True),
    bxFirst = cms.int32(-2),
    setBptxOR = cms.bool(True),
    bxLast = cms.int32(2),
    setBptxPlus = cms.bool(True),
    tcdsRecordLabel = cms.InputTag(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
