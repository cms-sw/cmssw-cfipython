import FWCore.ParameterSet.Config as cms

def PATMuonTimeLifeInfoProducer(*args, **kwargs):
  mod = cms.EDProducer('PATMuonTimeLifeInfoProducer',
    src = cms.InputTag('slimmedMuons'),
    pvSource = cms.InputTag('offlineSlimmedPrimaryVertices'),
    selection = cms.string(''),
    pvChoice = cms.int32(0),
    mightGet = cms.optional.untracked.vstring
  )
  for a in args:
    mod.update_(a)
  mod.update_(kwargs)
  return mod
