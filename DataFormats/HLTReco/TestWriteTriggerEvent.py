import FWCore.ParameterSet.Config as cms

def TestWriteTriggerEvent(**kwargs):
  mod = cms.EDProducer('TestWriteTriggerEvent',
    usedProcessName = cms.required.string,
    collectionTags = cms.required.vstring,
    collectionKeys = cms.required.vuint32,
    ids = cms.required.vint32,
    pts = cms.required.vdouble,
    etas = cms.required.vdouble,
    phis = cms.required.vdouble,
    masses = cms.required.vdouble,
    filterTags = cms.required.vstring,
    elementsPerVector = cms.required.uint32,
    filterIds = cms.required.vint32,
    filterKeys = cms.required.vuint32,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
