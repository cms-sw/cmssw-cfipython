import FWCore.ParameterSet.Config as cms

def PATTauTimeLifeInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('PATTauTimeLifeInfoProducer',
    src = cms.InputTag('slimmedTaus'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    selection = cms.string(''),
    pvChoice = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
