import FWCore.ParameterSet.Config as cms

def HLTDummyCollections(*args, **kwargs):
  mod = cms.EDProducer('HLTDummyCollections',
    action = cms.string(''),
    UnpackZDC = cms.bool(False),
    ESdigiCollection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
