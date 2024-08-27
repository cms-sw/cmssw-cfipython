import FWCore.ParameterSet.Config as cms

def PhotonMVAValueMapProducer(**kwargs):
  mod = cms.EDProducer('PhotonMVAValueMapProducer',
    src = cms.InputTag(''),
    keysForValueMaps = cms.InputTag(''),
    mvaConfigurations = cms.required.VPSet,
    mightGet = cms.optional.untracked.vstring
  )
  for k,v in kwargs.items():
    setattr(mod, k, v)
  return mod
