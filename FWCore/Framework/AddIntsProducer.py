import FWCore.ParameterSet.Config as cms

def AddIntsProducer(*args, **kwargs):
  mod = cms.EDProducer('AddIntsProducer',
    onlyGetOnEvent = cms.untracked.uint32(0),
    labels = cms.required.VInputTag,
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
