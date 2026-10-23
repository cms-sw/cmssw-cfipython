import FWCore.ParameterSet.Config as cms

def MuonViewCleaner(*args, **kwargs):
  mod = cms.EDProducer('MuonViewCleaner',
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
