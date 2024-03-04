import FWCore.ParameterSet.Config as cms

def PATMuonTimeLifeInfoProducer(**kwargs):
  mod = cms.EDProducer('PATMuonTimeLifeInfoProducer',
    src = cms.InputTag('slimmedMuons'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    selection = cms.string(''),
    pvChoice = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
