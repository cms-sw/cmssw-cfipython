import FWCore.ParameterSet.Config as cms

def PATTauTimeLifeInfoProducer(**kwargs):
  mod = cms.EDProducer('PATTauTimeLifeInfoProducer',
    src = cms.InputTag('slimmedTaus'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    selection = cms.string(''),
    pvChoice = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
