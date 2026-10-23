import FWCore.ParameterSet.Config as cms

def CandViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('CandViewCleaner',
    srcObject = cms.required.InputTag,
    srcObjectsToRemove = cms.required.VInputTag,
    deltaRMin = cms.required.double,
    srcObjectSelection = cms.string(''),
    srcObjectsToRemoveSelection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
