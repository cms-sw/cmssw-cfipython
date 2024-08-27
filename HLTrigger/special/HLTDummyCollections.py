import FWCore.ParameterSet.Config as cms

def HLTDummyCollections(**kwargs):
  mod = cms.EDProducer('HLTDummyCollections',
    action = cms.string(''),
    UnpackZDC = cms.bool(False),
    ESdigiCollection = cms.string(''),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
