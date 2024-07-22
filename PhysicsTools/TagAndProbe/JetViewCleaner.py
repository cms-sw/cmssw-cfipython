import FWCore.ParameterSet.Config as cms

def JetViewCleaner(**kwargs):
  mod = cms.EDProducer('JetViewCleaner',
    srcObject = cms.required.InputTag,
    srcObjectsToRemove = cms.required.VInputTag,
    deltaRMin = cms.required.double,
    srcObjectSelection = cms.string(''),
    srcObjectsToRemoveSelection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod