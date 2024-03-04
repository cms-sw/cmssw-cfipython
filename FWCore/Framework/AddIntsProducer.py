import FWCore.ParameterSet.Config as cms

def AddIntsProducer(**kwargs):
  mod = cms.EDProducer('AddIntsProducer',
    onlyGetOnEvent = cms.untracked.uint32(0),
    labels = cms.required.VInputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
