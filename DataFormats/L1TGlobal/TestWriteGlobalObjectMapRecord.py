import FWCore.ParameterSet.Config as cms

def TestWriteGlobalObjectMapRecord(**kwargs):
  mod = cms.EDProducer('TestWriteGlobalObjectMapRecord',
    nGlobalObjectMaps = cms.required.uint32,
    algoNames = cms.required.vstring,
    algoBitNumbers = cms.required.vint32,
    algoResults = cms.required.vint32,
    tokenNames0 = cms.required.vstring,
    tokenNumbers0 = cms.required.vint32,
    tokenResults0 = cms.required.vint32,
    tokenNames3 = cms.required.vstring,
    tokenNumbers3 = cms.required.vint32,
    tokenResults3 = cms.required.vint32,
    nElements1 = cms.required.uint32,
    nElements2 = cms.required.uint32,
    nElements3 = cms.required.uint32,
    firstElement = cms.required.int32,
    elementDelta = cms.required.int32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
